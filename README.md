# GetContact API Integration

A Streamlit-based web application for interacting with the GetContact API. This application provides a user-friendly interface to search for contacts and view their profiles using the GetContact service.

## Features

- User authentication system
- Secure API token management
- Contact search by phone number
- Detailed profile information display
- Modern and responsive UI
- Error handling and validation

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd getcontact-integration
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Open your browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Login with the following credentials:
   - Username: admin
   - Password: admin123

4. Add your GetContact API token in the Settings page

5. Start searching for contacts!

## Mock Mode

The application is configured to run in mock mode by default. This means it will return dummy data instead of making actual API calls. To use real API:

1. Obtain an official GetContact API token
2. Set `MOCK_MODE = False` in `config.py`
3. Add your API token in the application settings

## Project Structure

- `main.py` - Main application entry point
- `auth.py` - Authentication module
- `api_handler.py` - GetContact API interaction
- `ui.py` - Streamlit UI components
- `config.py` - Configuration settings

## Security Notes

- The current authentication system uses hardcoded credentials and is for demonstration purposes only
- In a production environment, implement proper user authentication
- Never commit API tokens to version control
- Consider using environment variables for sensitive data

## Created By

Letda Kes Dr. Sobri, S.Kom, CEH, OSCP, OSCE – Pegasus-Sobri Tool 