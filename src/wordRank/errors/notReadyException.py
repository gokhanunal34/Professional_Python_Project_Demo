"""
A custom exception class to note when an object isn't ready to perform
the operation being requested.
"""

class NotReadyException(Exception):
    """
    An exception class that is raised when a WordRank object is not ready
    to parse a file.
    """
    def __init__(self, message: str = "Not ready to perform the action."):
        self.msg = message
