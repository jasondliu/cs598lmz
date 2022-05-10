import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidArgumentError(Error):
    """Exception raised for invalid arguments.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class InvalidArgumentTypeError(InvalidArgumentError):
    """Exception raised for invalid argument types.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class InvalidArgumentValueError(InvalidArgumentError):
    """Exception raised for invalid argument values.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

