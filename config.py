from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """Centralized configuration for the GetContact Streamlit app."""

    admin_username: str = "admin"
    admin_password: str = "admin123"
    mock_mode: bool = True
    timeout_seconds: int = 10
    default_country_code: str = "+62"

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            admin_username=os.getenv("APP_ADMIN_USERNAME", "admin"),
            admin_password=os.getenv("APP_ADMIN_PASSWORD", "admin123"),
            mock_mode=os.getenv("MOCK_MODE", "true").lower() in {"1", "true", "yes"},
            timeout_seconds=int(os.getenv("GETCONTACT_TIMEOUT", "10")),
            default_country_code=os.getenv("DEFAULT_COUNTRY_CODE", "+62"),
        )
