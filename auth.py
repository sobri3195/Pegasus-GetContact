from __future__ import annotations

import hmac
from dataclasses import dataclass


@dataclass(frozen=True)
class Credentials:
    username: str
    password: str


def validate_login(input_cred: Credentials, expected_cred: Credentials) -> bool:
    """Constant-time credential comparison."""

    return hmac.compare_digest(input_cred.username, expected_cred.username) and hmac.compare_digest(
        input_cred.password,
        expected_cred.password,
    )


def mask_token(token: str, visible: int = 4) -> str:
    if not token:
        return ""
    visible = max(0, visible)
    if len(token) <= visible:
        return "*" * len(token)
    return "*" * (len(token) - visible) + token[-visible:]
