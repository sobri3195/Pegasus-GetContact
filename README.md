# GetContact API Integration

A Streamlit-based web app to authenticate users, store API tokens, and search contact profiles via GetContact.

## Fitur Utama

- Login admin sederhana
- Manajemen token API (simpan/hapus + masking)
- Normalisasi dan validasi nomor telepon
- Pencarian kontak (mock mode dan placeholder live mode)
- UI terpisah untuk Search dan Settings

## Menjalankan Aplikasi

```bash
python -m pip install streamlit
streamlit run main.py
```

Default credential:
- Username: `admin`
- Password: `admin123`

## Variabel Environment

- `APP_ADMIN_USERNAME` (default: `admin`)
- `APP_ADMIN_PASSWORD` (default: `admin123`)
- `MOCK_MODE` (default: `true`)
- `GETCONTACT_TIMEOUT` (default: `10`)
- `DEFAULT_COUNTRY_CODE` (default: `+62`)

## Pengujian

```bash
python -m unittest discover -s tests -v
```

## Struktur Modul

- `main.py`: entry point Streamlit
- `config.py`: konfigurasi aplikasi
- `auth.py`: autentikasi dan utilitas token
- `api_handler.py`: logika integrasi API
- `ui.py`: komponen antarmuka Streamlit
- `tests/test_core.py`: pengujian unit dasar
