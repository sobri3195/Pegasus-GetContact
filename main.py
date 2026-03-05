from __future__ import annotations

from config import AppConfig
from ui import initialize_session, render_login, render_search, render_settings


def run() -> None:
    import streamlit as st

    config = AppConfig.from_env()
    st.set_page_config(page_title="GetContact Integration", page_icon="📱", layout="centered")
    st.title("GetContact API Integration")
    st.caption("Kelola autentikasi, token API, dan pencarian kontak dalam satu dashboard.")

    initialize_session()

    if not st.session_state.authenticated:
        render_login(config)
        return

    st.sidebar.success("Authenticated")
    page = st.sidebar.radio("Navigasi", ["Search", "Settings"])

    if page == "Search":
        render_search(config)
    else:
        render_settings(config)


if __name__ == "__main__":
    run()
