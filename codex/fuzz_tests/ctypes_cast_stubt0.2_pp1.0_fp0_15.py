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
    """Exception raised for unimplemented features."""
    pass

class AttributeError(Error):
    """Exception raised for unimplemented features."""
    pass

class EOFError(Error):
    """Exception raised for unimplemented features."""
    pass

class FloatingPointError(Error):
    """Exception raised for unimplemented features."""
    pass

class GeneratorExit(Error):
    """Exception raised for unimplemented features."""
    pass

class ImportError(Error):
    """Exception raised for unimplemented features."""
    pass

class IndexError(Error):
    """Exception raised for unimplemented features."""
    pass

class KeyError(Error):
    """Exception raised for unimplemented features."""

