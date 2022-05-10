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
    """Exception raised when an attribute is not found."""
    pass

class ImportError(Error):
    """Exception raised when an import fails."""
    pass

class IndexError(Error):
    """Exception raised when an index is out of range."""
    pass

class KeyError(Error):
    """Exception raised when a key is not found."""
    pass

class KeyboardInterrupt(Error):
    """Exception raised when the user hits the interrupt key (normally Control-C or Delete)."""
    pass

class MemoryError(Error):
    """Exception raised when an operation runs out of memory."""
    pass

