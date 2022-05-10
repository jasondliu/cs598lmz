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

class ValueError(Error):
    """Exception raised for invalid values."""
    pass

class TypeError(Error):
    """Exception raised for invalid types."""
    pass

class IndexError(Error):
    """Exception raised for invalid indexes."""
    pass

class KeyError(Error):
    """Exception raised for invalid keys."""
    pass

class AttributeError(Error):
    """Exception raised for invalid attributes."""
    pass

class NameError(Error):
    """Exception raised for invalid names."""
    pass

class StopIteration(Error):
    """Exception raised to stop iteration."""
    pass

