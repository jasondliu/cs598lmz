import ctypes
import ctypes.util
import threading
import sqlite3

from . import _ffi
from . import _lib
from . import _util
from . import _compat
from . import _constants
from . import _errors
from . import _version
from . import _transaction
from . import _cursor
from . import _connection
from . import _backup


def _sqlite_version_check():
    """
    Check that the SQLite library is recent enough.
    """
    if _sqlite_version_info < _version.sqlite_version_info:
        raise _errors.InterfaceError(
            "SQLite %d.%d.%d or newer is required (found %r)" % (
                _version.sqlite_version_info + (_sqlite_version,)))


def _sqlite_version_info():
    """
    Return the version of the SQLite library as a tuple of (major, minor,
    patch).
    """
    return _lib.sqlite3_libversion_number()


_sqlite_version = _ffi.string(_lib.sqlite3_libversion()).dec
