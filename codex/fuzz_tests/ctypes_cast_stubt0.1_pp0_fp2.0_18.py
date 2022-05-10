import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotImplementedError(Error):
    """Exception raised for unimplemented features."""
    pass

class RuntimeError(Error):
    """Exception raised for unimplemented features."""
    pass

class TypeError(Error):
    """Exception raised for unimplemented features."""
    pass

class ValueError(Error):
    """Exception raised for unimplemented features."""
    pass

# ___________________________________________________________________________
# Functions

def abs(x):
    """abs(number) -> number

    Return the absolute value of the argument.
    """
    if x < 0:
        return -x
    return x

def all(iterable):
    """all(iterable) -> bool

    Return True if bool(x) is True for all values x in the iterable.
    """
    for x in iterable:
        if not x:
            return False
    return True
