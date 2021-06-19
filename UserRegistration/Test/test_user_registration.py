from UserRegistration.main.user_registrations import *

"""
-Added Test cases to check the following inputs.
"""


class TestUserRegistration:
    obj = User_Registration()

    def test_validate_firstName(self):
        result = self.obj.validate_first_name("Santosh")
        assert result == True

    def test_check_invalid_firstName(self):
        try:
            self.obj.validate_first_name("Sa")
        except:
            WrongInputException("Invalid input")

    def test_validate_lastName(self):
        result = self.obj.validate_last_name("Panda")
        assert result == True

    def test_check_invalid_lastName(self):
        try:
            self.obj.validate_last_name("panda")
        except:
            WrongInputException("Invalid input")

    def test_validate_email(self):
        result = self.obj.validate_email("santospanda111@gmail.com")
        assert result == True

    def test_check_invalid_email(self):
        try:
            self.obj.validate_email("abc@.com.my")
        except:
            WrongInputException("Invalid input")

    def test_validate_phone_number(self):
        result = self.obj.validate_phone_number("91 7978715564")
        assert result == True

    def test_check_invalid_phone_number(self):
        try:
            self.obj.validate_phone_number("7978")
        except:
            WrongInputException("Invalid input")

    def test_validate_password(self):
        result = self.obj.validate_password("Aabcdpanga12")
        assert result == True

    def test_check_invalid_password(self):
        try:
            self.obj.validate_password("ahjgfvhbbcd")
        except:
            WrongInputException("Invalid input")
