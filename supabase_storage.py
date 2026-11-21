import time
import uuid

import streamlit as st
from supabase import create_client

BUCKET_NAME = "interview-captures"
TABLE_NAME = "suspicious_events"


def new_session_id():
    """Makes a short random ID for one interview."""
    return uuid.uuid4().hex[:12]


@st.cache_resource
def get_client():
    """Connects to Supabase using the keys saved in Streamlit Secrets."""
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])


def save_event(session_id, event_time, reason, jpg_bytes):
    """Uploads one screenshot to the private bucket and saves its details in the table.
    Returns (True, None) on success or (False, error_text) on failure."""
    try:
        client = get_client()
        image_path = f"{session_id}/{int(time.time() * 1000)}_{reason}.jpg"

        client.storage.from_(BUCKET_NAME).upload(
            path=image_path,
            file=jpg_bytes,
            file_options={"content-type": "image/jpeg"},
        )

        client.table(TABLE_NAME).insert({
            "session_id": session_id,
            "event_time": event_time,
            "reason": reason,
            "image_path": image_path,
        }).execute()

        return True, None
    except Exception as e:
        return False, str(e)
