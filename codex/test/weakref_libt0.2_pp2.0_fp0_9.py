import weakref

from . import _core
from . import _util
from . import _types
from . import _errors
from . import _lib
from . import _ffi
from . import _compat

from . import _version
__version__ = _version.__version__

# -----------------------------------------------------------------------------
# Exceptions

class Error(_errors.Error):
    """Base class for all exceptions raised by this module."""
    pass

class InvalidStateError(Error):
    """Raised when an operation cannot be performed because the object is in
    an invalid state.
    """
    pass

class InvalidOperationError(Error):
    """Raised when an operation cannot be performed because the object is in
    an invalid state.
    """
    pass

class InvalidArgumentError(Error):
    """Raised when an invalid argument is passed to a function."""
    pass

class InvalidNameError(Error):
    """Raised when an invalid name is passed to a function."""
