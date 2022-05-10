import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotImplementedError(Error):
    """Exception raised for unimplemented functionality.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class NotImplementedWarning(Warning):
    """Warning raised for unimplemented functionality.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class NotImplemented(object):
    """
    A class to represent unimplemented functionality.
    """
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(self, "Unimplemented functionality.")
