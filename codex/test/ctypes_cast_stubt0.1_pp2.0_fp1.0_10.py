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

class AssertionError(Error):
    """Exception raised for failed assertions."""
    pass

class AttributeError(Error):
    """Exception raised for failed attribute references."""
    pass

class EOFError(Error):
    """Exception raised for end of file."""
    pass

class FloatingPointError(Error):
    """Exception raised for floating point errors."""
    pass

class GeneratorExit(Error):
    """Exception raised for generator exit."""
    pass

class ImportError(Error):
    """Exception raised for failed imports."""
    pass

class IndexError(Error):
    """Exception raised for invalid indexes."""
    pass

class KeyError(Error):
    """Exception raised for invalid keys."""
    pass

