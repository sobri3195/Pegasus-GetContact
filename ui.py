from __future__ import annotations

from auth import Credentials, mask_token, validate_login
from config import AppConfig
from api_handler import GetContactClient


def _require_streamlit():
    import streamlit as st

    return st


def initialize_session() -> None:
    st = _require_streamlit()
    st.session_state.setdefault("authenticated", False)
    st.session_state.setdefault("api_token", "")


def render_login(config: AppConfig) -> None:
    st = _require_streamlit()
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Masuk", type="primary"):
        if validate_login(
            Credentials(username=username, password=password),
            Credentials(username=config.admin_username, password=config.admin_password),
        ):
            st.session_state.authenticated = True
            st.success("Login berhasil")
            st.rerun()
        else:
            st.error("Username atau password salah")


def render_settings(config: AppConfig) -> None:
    st = _require_streamlit()
    st.subheader("Settings")

    current = st.session_state.api_token
    st.caption(f"Token tersimpan: `{mask_token(current) or '(belum ada)'}`")
    new_token = st.text_input("GetContact API Token", value=current, type="password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Simpan Token"):
            st.session_state.api_token = new_token.strip()
            st.success("Token disimpan")
    with col2:
        if st.button("Hapus Token"):
            st.session_state.api_token = ""
            st.success("Token dihapus")

    mode = "Mock" if config.mock_mode else "Live"
    st.info(f"Mode aplikasi aktif: **{mode}**")


def render_search(config: AppConfig) -> None:
    st = _require_streamlit()
    st.subheader("Cari Kontak")
    phone = st.text_input("Nomor Telepon", placeholder="08123456789 atau +628123456789")

    if st.button("Cari"):
        client = GetContactClient(token=st.session_state.api_token, mock_mode=config.mock_mode)
        try:
            result = client.search_contact(phone, default_country_code=config.default_country_code)
            st.success("Kontak ditemukan")
            st.json(result)
        except Exception as exc:  # noqa: BLE001
            st.error(str(exc))
