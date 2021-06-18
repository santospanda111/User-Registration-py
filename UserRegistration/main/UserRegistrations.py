import re

from UserRegistration.main.WrongInputException import WrongInputException


class User_Registration:
    """
    Created a class for validating user registration
    """
    FIRST_NAME_PATTERN = r'^[A-Z]{1}[a-z]{2,}$'
    LAST_NAME_PATTERN = r'^[A-Z]{1}[a-z]{2,}$'

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


if __name__ == "__main__":
    print("Welcome to User-Registration Program")
