# technical_interview.py
# المقابلة التقنية - الإجابات والنتايج بتتحفظ في st.session_state بس

import os

import streamlit as st
import streamlit.components.v1 as components

from question_bank import QUESTION_BANK
from keyword_synonyms import keyword_present

# تحميل صندوق الكلام (الملف speech_component/index.html)
_COMPONENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "speech_component")
speech_answer = components.declare_component("speech_answer", path=_COMPONENT_DIR)

PREFIX = "tech_"


def _reset_interview():
    for key in list(st.session_state.keys()):
        if key.startswith(PREFIX):
            del st.session_state[key]


def evaluate_answer(answer, keywords):
    """تقييم بسيط بالكلمات المفتاحية. بيرجع: الدرجة، الكلمات الموجودة، الكلمات الناقصة"""
    text = (answer or "").lower()
    found = [k for k in keywords if keyword_present(k, answer)]
    missing = [k for k in keywords if not keyword_present(k, answer)]
    coverage = len(found) / len(keywords) if keywords else 0

    words_count = len(text.split())
    if words_count >= 25:
        completeness = 1.0
    elif words_count >= 10:
        completeness = 0.6
    elif words_count > 0:
        completeness = 0.3
    else:
        completeness = 0.0

    # 80% للكلمات المفتاحية + 20% لاكتمال الإجابة
    score = round((coverage * 0.8 + completeness * 0.2) * 100)
    return score, found, missing


def _grade_label(score):
    if score >= 80:
        return "ممتاز"
    if score >= 60:
        return "جيد"
    if score >= 40:
        return "مقبول"
    return "ضعيف"


def render_technical_interview():
    st.header("Technical Interview / المقابلة التقنية")

    state = PREFIX + "state"
    if state not in st.session_state:
        st.session_state[state] = "setup"

    # ---------- 1) اختيار التخصص والمستوى ----------
    if st.session_state[state] == "setup":
        track = st.selectbox("Specialization / التخصص", list(QUESTION_BANK.keys()))
        level = st.selectbox("Level / المستوى", ["Beginner", "Intermediate", "Advanced"])
        speech_lang = st.selectbox("Answer language / لغة الإجابة", ["English (US)", "العربية (مصر)"])
        if st.button("Start Technical Interview"):
            st.session_state[PREFIX + "track"] = track
            st.session_state[PREFIX + "level"] = level
            st.session_state[PREFIX + "lang"] = "en-US" if speech_lang == "English (US)" else "ar-EG"
            st.session_state[PREFIX + "questions"] = QUESTION_BANK[track][level]
            st.session_state[PREFIX + "index"] = 0
            st.session_state[PREFIX + "answers"] = {}
            st.session_state[state] = "running"
            st.rerun()
        return

    questions = st.session_state[PREFIX + "questions"]
    idx = st.session_state[PREFIX + "index"]

    # ---------- 2) الأسئلة ----------
    if st.session_state[state] == "running":
        q = questions[idx]
        st.progress(idx / len(questions))
        st.subheader(f"Question {idx + 1} of {len(questions)}")
        st.write(q["question"])

        answer_text = speech_answer(
            lang=st.session_state[PREFIX + "lang"],
            key=f"{PREFIX}speech_{idx}",
            default="",
        )
        st.session_state[PREFIX + "answers"][idx] = answer_text or ""

        st.markdown("**Your answer / إجابتك:**")
        if answer_text:
            st.info(answer_text)
        else:
            st.caption("اضغط (ابدأ الإجابة) واتكلم، وبعدين اضغط (إيقاف). الإجابة هتظهر هنا.")

        is_last = idx == len(questions) - 1
        if st.button("Finish and show report" if is_last else "Next question"):
            if is_last:
                st.session_state[state] = "report"
            else:
                st.session_state[PREFIX + "index"] = idx + 1
            st.rerun()
        return

    # ---------- 3) التقرير ----------
    if st.session_state[state] == "report":
        st.subheader("Evaluation Report / تقرير التقييم")
        st.write(
            f"**Track:** {st.session_state[PREFIX + 'track']}  |  "
            f"**Level:** {st.session_state[PREFIX + 'level']}"
        )

        scores = []
        for i, q in enumerate(questions):
            answer = st.session_state[PREFIX + "answers"].get(i, "")
            score, found, missing = evaluate_answer(answer, q["keywords"])
            scores.append(score)
            with st.expander(f"Q{i + 1}: {q['question']}  —  {score}%", expanded=True):
                st.markdown(f"**Your answer:** {answer if answer else '(no answer)'}")
                st.markdown(f"**Model answer:** {q['model_answer']}")
                st.markdown(f"**Keywords found:** {', '.join(found) if found else '-'}")
                st.markdown(f"**Keywords missing:** {', '.join(missing) if missing else '-'}")

        final = round(sum(scores) / len(scores)) if scores else 0
        st.metric("Final score / الدرجة النهائية", f"{final}%")
        st.success(f"التقدير: {_grade_label(final)}")

        if st.button("Start a new interview"):
            _reset_interview()
            st.rerun()
