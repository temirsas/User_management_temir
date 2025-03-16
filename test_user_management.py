import unittest
from datetime import datetime
from user import User
from user_service import UserService
from user_util import UserUtil


class TestUserManagementSystem(unittest.TestCase):

    def setUp(self):
        self.user_id = UserUtil.generate_user_id()
        self.user = User(self.user_id, "Temir", "Saidulaev", datetime(2005, 3, 21))
        self.user.email = UserUtil.generate_email("Temir", "Saidulaev", "gmail.com")
        self.user.password = UserUtil.generate_password()

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Temir")
        self.assertEqual(self.user.surname, "Saidulaev")
        self.assertEqual(self.user.get_age(), datetime.now().year - 2005)

    def test_user_service(self):
        UserService.add_user(self.user)
        self.assertEqual(UserService.get_number(), 1)

        found_user = UserService.find_user(self.user_id)
        self.assertIsNotNone(found_user)

        UserService.delete_user(self.user_id)
        self.assertIsNone(UserService.find_user(self.user_id))
        self.assertEqual(UserService.get_number(), 0)

    def test_user_update(self):
        UserService.add_user(self.user)
        updated_user = User(self.user_id, "Temir", "Saidulaev", datetime(2005, 3, 21))
        UserService.update_user(self.user_id, updated_user)
        self.assertEqual(UserService.find_user(self.user_id).name, "Temir")

    def test_util_methods(self):
        self.assertEqual(len(UserUtil.generate_user_id()), 9)
        self.assertTrue(UserUtil.is_strong_password(UserUtil.generate_password()))
        self.assertTrue(UserUtil.validate_email(self.user.email))
        self.assertFalse(UserUtil.validate_email("invalid-email"))


if __name__ == '__main__':
    unittest.main()
