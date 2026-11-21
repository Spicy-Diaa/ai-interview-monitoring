import os
import threading
import time

import av
import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision
from streamlit_webrtc import VideoProcessorBase, webrtc_streamer
from supabase_storage import new_session_id, save_event

# ---------------- Settings (same values as monitor.py) ----------------
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "face_landmarker.task")

HEAD_TURN_LIMIT = 0.20
GAZE_LIMIT = 0.05
SUSPICIOUS_SECONDS = 0.5
COOLDOWN_SECONDS = 2.0
GRACE_SECONDS = 0.7

DETECT_WIDTH = 320        # frames are shrunk to this width before detection (faster)
DETECT_EVERY = 3          # run the face model on 1 of every 3 frames (the server is weak)
MAX_SNAPSHOTS = 12        # snapshots kept in memory for display

# Speech language for the browser (Chrome/Edge): "ar-EG" Egyptian, "ar-SA" Saudi, "en-US" English
LANGUAGE_CODE = "ar-EG"

def build_rtc_config():
    """STUN helps most networks connect; TURN relays the video when a network blocks direct connections."""
    servers = [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]},
    ]
    try:
        # your own free TURN account (see the steps): put these 2 values in the app's Secrets
        user = st.secrets["TURN_USERNAME"]
        cred = st.secrets["TURN_CREDENTIAL"]
        host = st.secrets.get("TURN_HOST", "global.relay.metered.ca")
        servers += [
            {"urls": [f"turn:{host}:80"], "username": user, "credential": cred},
            {"urls": [f"turn:{host}:80?transport=tcp"], "username": user, "credential": cred},
            {"urls": [f"turn:{host}:443"], "username": user, "credential": cred},
            {"urls": [f"turns:{host}:443?transport=tcp"], "username": user, "credential": cred},
        ]
    except Exception:
        # no secrets set: try the public Open Relay test server (may be limited or unavailable)
        servers.append({
            "urls": ["turn:openrelay.metered.ca:80", "turn:openrelay.metered.ca:443",
                     "turn:openrelay.metered.ca:443?transport=tcp"],
            "username": "openrelayproject",
            "credential": "openrelayproject",
        })
    return {"iceServers": servers}


RTC_CONFIGURATION = build_rtc_config()


# ---------------- Detection logic (copied from monitor.py) ----------------
def analyze_face(lm):
    left = lm[234].x
    right = lm[454].x
    nose = lm[1].x

    face_w = max(right - left, 1e-6)
    head_offset = ((nose - left) / face_w) - 0.5

    def eye_ratio(iris, c1, c2):
        a = lm[c1].x
        b = lm[c2].x
        w = max(abs(b - a), 1e-6)
        return ((lm[iris].x - min(a, b)) / w) - 0.5

    gaze_offset = (
        eye_ratio(468, 33, 133) +
        eye_ratio(473, 362, 263)
    ) / 2

    return head_offset, gaze_offset


class InterviewProcessor(VideoProcessorBase):
    """Runs for every video frame that arrives from the browser camera."""

    def __init__(self):
        options = vision.FaceLandmarkerOptions(
            base_options=mp_python.BaseOptions(model_asset_path=MODEL_PATH),
            running_mode=vision.RunningMode.IMAGE,
            num_faces=2,
        )
        self.landmarker = vision.FaceLandmarker.create_from_options(options)

        self.lock = threading.Lock()
        self.events_count = 0
        self.snapshots = []          # list of (time_str, reason, jpg_bytes)

        self.suspicious_since = None
        self.last_saved = 0.0
        self.last_seen_bad = 0.0

        self.frame_i = 0
        self.cache = (None, None, None)     # last (reason, head, gaze)

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        self.frame_i += 1
        if self.frame_i % DETECT_EVERY == 1:
            h, w = img.shape[:2]
            small = cv2.resize(img, (DETECT_WIDTH, int(h * DETECT_WIDTH / w)))
            rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

            faces = self.landmarker.detect(mp_image).face_landmarks
            reason, head, gaze = None, None, None

            if len(faces) == 0:
                reason = "no_face"
            elif len(faces) > 1:
                reason = "multiple_faces"
            else:
                head, gaze = analyze_face(faces[0])
                if abs(head) > HEAD_TURN_LIMIT:
                    reason = "head_turned"
                elif abs(gaze) > GAZE_LIMIT:
                    reason = "looking_away"
            self.cache = (reason, head, gaze)

        reason, head, gaze = self.cache
        if head is not None:
            cv2.putText(img, f"head={head:.2f} gaze={gaze:.2f}", (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        now = time.time()

        if reason:
            self.last_seen_bad = now
            if self.suspicious_since is None:
                self.suspicious_since = now
            elapsed = now - self.suspicious_since

            cv2.putText(img, f"WARNING: {reason}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            if elapsed >= SUSPICIOUS_SECONDS and now - self.last_saved >= COOLDOWN_SECONDS:
                ok, buf = cv2.imencode(".jpg", img)
                if ok:
                    with self.lock:
                        self.snapshots.append(
                            (time.strftime("%H:%M:%S"), reason, buf.tobytes())
                        )
                        self.snapshots = self.snapshots[-MAX_SNAPSHOTS:]
                        self.events_count += 1
                self.last_saved = now
        else:
            if self.suspicious_since is not None and now - self.last_seen_bad > GRACE_SECONDS:
                self.suspicious_since = None
            cv2.putText(img, "OK", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2)

        cv2.putText(img, f"Potential events: {self.events_count}", (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 128, 255), 2)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


SPEECH_HTML = """
<div style="font-family:Arial,sans-serif">
  <button id="btn" style="padding:10px 18px;font-size:16px;border:0;border-radius:6px;
          background:#c9304a;color:#fff;cursor:pointer">ابدأ تحويل الكلام إلى نص</button>
  <span id="status" style="margin-inline-start:12px;color:#666;font-size:14px"></span>
  <div dir="rtl" style="margin-top:12px;padding:12px;border:1px solid #ddd;border-radius:8px;
       min-height:90px;max-height:220px;overflow-y:auto;font-size:22px">
    <div style="font-size:17px;font-weight:bold;color:#c9304a;margin-bottom:10px;padding-bottom:8px;border-bottom:2px solid #f3d3d9">🎙️ النص المباشر · Live Transcript</div>
    <div id="lines"></div>
    <div id="interim" style="color:#999"></div>
  </div>
</div>
<script>
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const btn = document.getElementById("btn");
const statusEl = document.getElementById("status");
const linesEl = document.getElementById("lines");
const interimEl = document.getElementById("interim");
let rec = null, active = false, running = false;

function setStatus(t) { statusEl.textContent = t; }

function addLine(text) {
  if (!text) return;
  const d = document.createElement("div");
  const t = new Date().toLocaleTimeString("en-GB");
  d.innerHTML = "<small style='color:#888'>" + t + "</small> &nbsp; ";
  d.appendChild(document.createTextNode(text));
  linesEl.appendChild(d);
  linesEl.parentElement.scrollTop = linesEl.parentElement.scrollHeight;
}

// Chrome ends a listening session every now and then (silence, time limit, network).
// So we create a fresh recognizer and start it again whenever it ends.
function startSession() {
  if (!active || running) return;
  rec = new SR();
  rec.lang = "__LANG__";
  rec.continuous = true;
  rec.interimResults = true;
  rec.onstart = () => { running = true; setStatus("🎤 يستمع... اتكلم"); };
  rec.onresult = (e) => {
    let interim = "";
    for (let i = e.resultIndex; i < e.results.length; i++) {
      const r = e.results[i];
      if (r.isFinal) addLine(r[0].transcript.trim());
      else interim += r[0].transcript;
    }
    interimEl.textContent = interim;
  };
  rec.onerror = (e) => {
    if (e.error === "no-speech" || e.error === "aborted") return;   // normal, restarts below
    setStatus("خطأ: " + e.error);
    if (e.error === "not-allowed" || e.error === "service-not-allowed") active = false;
  };
  rec.onend = () => {
    running = false;
    interimEl.textContent = "";
    if (active) setTimeout(startSession, 300);
    else { setStatus("متوقف"); btn.textContent = "ابدأ تحويل الكلام إلى نص"; }
  };
  try { rec.start(); } catch (_) { running = false; }
}

// safety net: if the session died without telling us, start it again
setInterval(() => { if (active && !running) startSession(); }, 2000);

btn.onclick = () => {
  if (!SR) { setStatus("المتصفح لا يدعم التعرف على الكلام. استخدم Chrome أو Edge."); return; }
  if (active) { active = false; if (rec) rec.stop(); }
  else { active = true; btn.textContent = "إيقاف"; startSession(); }
};
</script>
"""


# ---------------- Page ----------------
st.set_page_config(page_title="Interview Monitor", layout="wide")
st.title("Interview Monitor")

st.info(
    "Privacy notice: your camera is analysed to detect head turns, looking away, "
    "no face, or multiple faces. If you also allow the microphone, your speech is sent "
    "to Google's speech recognition and shown as text. Nothing is stored on disk; "
    "snapshots and text stay in this session only. These events need human review; "
    "they are not proof of misconduct."
)

consent = st.checkbox("I consent to webcam monitoring")
mic_consent = st.checkbox("Also record my voice and convert it to text (microphone)")

if consent:
    ctx = webrtc_streamer(
        key="interview-monitor",
        video_processor_factory=InterviewProcessor,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": {"width": {"ideal": 320}, "height": {"ideal": 240}, "frameRate": {"ideal": 12}},
            "audio": False,
        },
        video_html_attrs={
            "style": {"width": "400px", "max-width": "100%", "margin": "0 auto", "display": "block"},
            "controls": False,
            "autoPlay": True,
        },
        async_processing=True,
    )

    if mic_consent:
        # Speech-to-text runs inside the person's own browser (Chrome/Edge), not on the server
                    
        speech_choice = st.selectbox("Speech language / لغة الكلام", ["العربية (مصر)", "English (US)"])
        lang_code = "ar-EG" if speech_choice == "العربية (مصر)" else "en-US"
        components.html(SPEECH_HTML.replace("__LANG__", lang_code), height=330)
    events_box = st.empty()
    shots_box = st.empty()

    while ctx.state.playing:
        proc = ctx.video_processor
        if proc is not None:
            with proc.lock:
                count = proc.events_count
                shots = list(proc.snapshots)
                 # --- Save new suspicious screenshots to Supabase ---
            if "session_id" not in st.session_state:
                st.session_state["session_id"] = new_session_id()
                st.session_state["uploaded_count"] = 0
            if count < st.session_state["uploaded_count"]:
                st.session_state["uploaded_count"] = 0
            new_n = count - st.session_state["uploaded_count"]
            if new_n > 0:
                for t, reason, jpg in shots[-new_n:]:
                    ok, err = save_event(st.session_state["session_id"], t, reason, jpg)
                    if not ok:
                        st.toast(f"Supabase save failed: {err}")
                st.session_state["uploaded_count"] = count               
            events_box.metric("Potential events", count)
            with shots_box.container():
                if shots:
                    cols = st.columns(4)
                    for i, (t, reason, jpg) in enumerate(reversed(shots)):
                        cols[i % 4].image(jpg, caption=f"{t} - {reason}")
        time.sleep(1)
else:
    st.warning("Tick the consent box to start the camera.")
