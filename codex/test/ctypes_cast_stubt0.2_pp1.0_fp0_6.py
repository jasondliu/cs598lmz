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
    """Exception raised for runtime errors."""
    pass

class TypeError(Error):
    """Exception raised for type errors."""
    pass

class ValueError(Error):
    """Exception raised for value errors."""
    pass

class OverflowError(Error):
    """Exception raised for overflow errors."""
    pass

class ZeroDivisionError(Error):
    """Exception raised for zero division errors."""
    pass

class AssertionError(Error):
    """Exception raised for assertion errors."""
    pass

class AttributeError(Error):
    """Exception raised for attribute errors."""
    pass

class ImportError(Error):
    """Exception raised for import errors."""
    pass

