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
    """Exception raised when an attribute reference or assignment fails."""
    pass

class EOFError(Error):
    """Exception raised when the input file is empty."""
    pass

class FloatingPointError(Error):
    """Exception raised when a floating point calculation fails."""
    pass

class IOError(Error):
    """Exception raised when an I/O operation fails."""
    pass

class ImportError(Error):
    """Exception raised when an import statement fails."""
    pass

class IndexError(Error):
    """Exception raised when an index is not found."""
    pass

