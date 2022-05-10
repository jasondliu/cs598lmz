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

class StopIteration(Error):
    """Exception raised for unimplemented features."""
    pass

# ___________________________________________________________________________
# Functions

def abs(x):
    """Return the absolute value of the argument."""
    return x if x >= 0 else -x

def all(iterable):
    """Return True if bool(x) is True for all values x in the iterable."""
    for element in iterable:
        if not element:
            return False
    return True


