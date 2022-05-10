import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotImplementedError(Error):
    """Exception raised for unimplemented functionality."""
    pass

class NotImplementedWarning(Warning):
    """Exception raised for unimplemented functionality."""
    pass

class NotImplemented(object):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(*args, **kwargs)

class NotImplementedWarning(Warning):
    def __init__(self, *args, **kwargs):
        raise NotImplementedWarning(*args, **kwargs)

# ___________________________________________________________________________
# Functions

def get_func_name():
    """Return the name of the function that called the function that called
    this function."""
    return sys._getframe(2).f_code.co_name

