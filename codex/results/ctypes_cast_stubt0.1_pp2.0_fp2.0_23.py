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

class UnsupportedError(Error):
    """Exception raised for unsupported features."""
    pass

class NotSupportedError(Error):
    """Exception raised for unsupported features."""
    pass

class NotFoundError(Error):
    """Exception raised for missing features."""
    pass

class NotAvailableError(Error):
    """Exception raised for missing features."""
    pass

class NotInstalledError(Error):
    """Exception raised for missing features."""
    pass

class NotConfiguredError(Error):
    """Exception raised for missing features."""
    pass

class NotReadyError(Error):
    """Exception raised for missing features."""
    pass

class NotInitializedError(Error):
    """Exception raised for missing features."""
    pass

class NotLoadedError(Error
