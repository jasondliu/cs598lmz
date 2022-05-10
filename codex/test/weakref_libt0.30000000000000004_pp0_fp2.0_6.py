import weakref

from . import _core
from . import _util
from . import _errors
from . import _types
from . import _constants
from . import _lib

from . import _version
__version__ = _version.__version__

#------------------------------------------------------------------------------
# Exceptions

class Error(Exception):
    """Base class for all exceptions in this module."""
    pass

class InvalidHandleError(Error):
    """Raised when a handle is not valid."""
    pass

class InvalidParamError(Error):
    """Raised when a parameter is not valid."""
    pass

class InvalidStateError(Error):
    """Raised when a state is not valid."""
    pass

class InvalidValueError(Error):
    """Raised when a value is not valid."""
    pass

class InvalidStringError(Error):
    """Raised when a string is not valid."""
    pass

class InvalidBufferError(Error):
    """Raised when a buffer is not valid."""
    pass

