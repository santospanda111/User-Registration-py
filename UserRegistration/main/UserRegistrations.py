import re

from UserRegistration.main.WrongInputException import WrongInputException


class User_Registration:
    """
    Created a class for validating user registration
    """
    FIRST_NAME_PATTERN = r'^[A-Z]{1}[a-z]{2,}$'
    LAST_NAME_PATTERN = r'^[A-Z]{1}[a-z]{2,}$'
    EMAIL_PATTERN = r'^[A-Za-z0-9]+([-.+_]{1}[0-9A-Za-z]+)*[@][A-Za-z0-9]+[.][a-zA-Z]{2,4}([.,]{1}[a-z]{2,3}){0,1}$'
    PHONE_NUMBER_PATTERN = r'^[0-9]{1,3} [0-9]{10}$'

    def validate_first_name(self, first_name):
        """
        :param first_name:
        :return: if first name matches with pattern, return True
        """
        try:
            pattern = re.compile(self.FIRST_NAME_PATTERN)
            match = pattern.search(first_name)
            if not match:
                return False
            else:
                return True
        except WrongInputException as e:
            print(e)

    def validate_last_name(self, last_name):
        """
        :param last_name:
        :return: if last name matches with pattern, return True
        """
        try:
            pattern = re.compile(self.LAST_NAME_PATTERN)
            match = pattern.search(last_name)
            if not match:
                return False
            else:
                return True
        except WrongInputException as e:
            print(e)

    def validate_email(self, email):
        """
        :param email:
        :return: if email matches with pattern, return True
        """
        try:
            pattern = re.compile(self.EMAIL_PATTERN)
            match = pattern.search(email)
            if not match:
                return False
            else:
                return True
        except WrongInputException as e:
            print(e)

    def validate_phone_number(self, phone_number):
        """
        :param phone_number:
        :return: if phone_number matches with pattern, return True
        """
        try:
            pattern = re.compile(self.PHONE_NUMBER_PATTERN)
            match = pattern.search(phone_number)
            if not match:
                return False
            else:
                return True
        except WrongInputException as e:
            print(e)


if __name__ == "__main__":
    print("Welcome to User-Registration Program")
