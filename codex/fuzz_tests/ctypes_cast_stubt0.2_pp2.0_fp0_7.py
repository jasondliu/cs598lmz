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

class TypeError(Error):
    """Exception raised for type errors."""
    pass

class ValueError(Error):
    """Exception raised for value errors."""
    pass

class KeyError(Error):
    """Exception raised for key errors."""
    pass

class IndexError(Error):
    """Exception raised for index errors."""
    pass

class AttributeError(Error):
    """Exception raised for attribute errors."""
    pass

class RuntimeError(Error):
    """Exception raised for runtime errors."""
    pass

class NotImplementedError(Error):
    """Exception raised for unimplemented features."""
    pass

class NameError(Error):
    """Exception raised for undefined names."""
    pass

class ZeroDivisionError(Error):
    """
