import _struct

from . import _pylibpd as pd

from .constants import *
from .patch import Patch
from . import _pylibpd

from . import libpd

################################################################################
# Exceptions
################################################################################

class PdException(Exception):
    """Base class for pylibpd exceptions."""
    pass

class PdInitError(PdException):
    """Raised when an error occurs while initializing libpd."""
    pass

class PdArgumentError(PdException):
    """Raised when a wrong argument is passed to a libpd function."""
    pass

class PdPatchError(PdException):
    """Raised when a patch cannot be opened."""
    pass

################################################################################
# Helper functions
################################################################################

def _check(return_value):
    """Check the return value of a libpd function.
    
    If the return value is negative, raise an exception.
    """
