from UserRegistration.main.UserRegistrations import *

"""
-Added Test cases to check the following inputs.
"""


class TestUserRegistration:
    obj = User_Registration()

    def test_validate_FirstName(self):
        result = self.obj.validate_first_name("Santosh")
        assert result == True

    def test_check_Invalid_FirstName(self):
        result = self.obj.validate_first_name("Sa")
        assert result == False

    def test_validate_LastName(self):
        result = self.obj.validate_last_name("Panda")
        assert result == True

    def test_check_Invalid_LastName(self):
        result = self.obj.validate_last_name("panda")
        assert result == False
