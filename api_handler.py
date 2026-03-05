from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from typing import Dict


_PHONE_PATTERN = re.compile(r"^\+?[1-9]\d{7,14}$")


@dataclass
class ContactProfile:
    phone_number: str
    display_name: str
    tags: list[str]
    confidence: float

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


class GetContactClient:
    def __init__(self, token: str = "", mock_mode: bool = True) -> None:
        self.token = token
        self.mock_mode = mock_mode

    @staticmethod
    def normalize_phone(phone_number: str, default_country_code: str = "+62") -> str:
        value = (phone_number or "").strip().replace(" ", "")
        if value.startswith("0"):
            value = f"{default_country_code}{value[1:]}"
        if not value.startswith("+") and value.isdigit():
            value = f"+{value}"
        return value

    @staticmethod
    def validate_phone(phone_number: str) -> None:
        if not _PHONE_PATTERN.match(phone_number):
            raise ValueError("Nomor telepon tidak valid. Gunakan format internasional, misalnya +628123456789")

    def search_contact(self, phone_number: str, default_country_code: str = "+62") -> Dict[str, object]:
        normalized = self.normalize_phone(phone_number, default_country_code)
        self.validate_phone(normalized)

        if self.mock_mode:
            return ContactProfile(
                phone_number=normalized,
                display_name="Mock User",
                tags=["Personal", "Indonesia"],
                confidence=0.89,
            ).to_dict()

        if not self.token:
            raise PermissionError("API token belum disetel. Buka Settings untuk menyimpan token.")

        # Placeholder for real integration.
        return ContactProfile(
            phone_number=normalized,
            display_name="Live API (placeholder)",
            tags=["Unknown"],
            confidence=0.0,
        ).to_dict()
