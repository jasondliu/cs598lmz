import gc, weakref

from . import _util
from ._util import _import_c_accel

_c_accel = _import_c_accel()

#----------------------------------------------------------------------------
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidShapeError(Error):
    """Exception raised when a shape is invalid."""
    pass

class InvalidDimensionError(Error):
    """Exception raised when a dimension is invalid."""
    pass

class InvalidTypeError(Error):
    """Exception raised when a type is invalid."""
    pass

class InvalidValueError(Error):
    """Exception raised when a value is invalid."""
    pass

class InvalidIndexError(Error):
    """Exception raised when an index is invalid."""
    pass

class InvalidOperationError(Error):
    """Exception raised when an operation is invalid."""
    pass

class InvalidArgumentError(Error):
    """Exception raised when an argument is invalid."""
    pass

class InvalidResultError(Error):
    """Exception raised when a result is invalid
