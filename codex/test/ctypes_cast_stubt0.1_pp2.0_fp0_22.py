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

class NotImplementedByDesignWarning(Warning):
    """Exception raised for unimplemented functionality."""
    pass

class NotImplementedByDesignError(Error):
    """Exception raised for unimplemented functionality."""
    pass

class NotImplementedYetWarning(Warning):
    """Exception raised for unimplemented functionality."""
    pass

class NotImplementedYetError(Error):
    """Exception raised for unimplemented functionality."""
    pass

class NotImplementedInThisVersionWarning(Warning):
    """Exception raised for unimplemented functionality."""
    pass

