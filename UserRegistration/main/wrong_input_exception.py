class WrongInputException(Exception):
    """
    Creating class for custom errors inherited from Exception class
    """

    def __init__(self, message):
        """
        -Message is inherited from Exception class
        :param message:
        """
        super.__init__(message)
