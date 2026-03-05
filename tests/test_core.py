import unittest

from api_handler import GetContactClient
from auth import Credentials, mask_token, validate_login


class AuthTests(unittest.TestCase):
    def test_validate_login_true(self):
        self.assertTrue(
            validate_login(Credentials("admin", "pass"), Credentials("admin", "pass"))
        )

    def test_validate_login_false(self):
        self.assertFalse(
            validate_login(Credentials("admin", "wrong"), Credentials("admin", "pass"))
        )

    def test_mask_token(self):
        self.assertEqual(mask_token("abcdef1234"), "******1234")


class ApiTests(unittest.TestCase):
    def test_normalize_phone(self):
        self.assertEqual(GetContactClient.normalize_phone("08123456789"), "+628123456789")

    def test_search_contact_mock(self):
        data = GetContactClient(mock_mode=True).search_contact("+628123456789")
        self.assertEqual(data["display_name"], "Mock User")

    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            GetContactClient(mock_mode=True).search_contact("123")


if __name__ == "__main__":
    unittest.main()
