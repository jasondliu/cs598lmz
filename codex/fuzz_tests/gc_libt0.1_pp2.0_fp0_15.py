import gc, weakref

from . import _core
from . import _util
from . import _types
from . import _errors
from . import _compat
from . import _constants
from . import _lib
from . import _version

from . import _lazy_import
_lazy_import.lazy_import(globals(), """
import sys

from . import _util
from . import _types
from . import _errors
from . import _compat
from . import _constants
from . import _lib
from . import _version
""")

#------------------------------------------------------------------------------
# Exceptions
#------------------------------------------------------------------------------

class Error(_errors.Error):
    """Base class for all exceptions raised by this module."""

class InterfaceError(Error):
    """Exception raised for errors that are related to the database interface
    rather than the database itself.  E.g. this error is raised if a method
    requires a database connection and none is available."""

class DatabaseError(Error):
    """Exception raised for errors that are related to the database."""

class InternalError(DatabaseError):
    """Exception
