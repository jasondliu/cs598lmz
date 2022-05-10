import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

from . import _sqlite3

def _assert_threadsafety():
    """
    Check that sqlite3 was compiled with the correct threading options.
    """
    if _sqlite3.sqlite_version_info < (3, 6, 0):
        # SQLite was not compiled with SQLITE_THREADSAFE
        if _sqlite3.sqlite_threadsafe() == 0:
            raise sqlite3.ProgrammingError("SQLite 3.6.0 or newer is required "
                                           "(found %s)." %
                                           _sqlite3.sqlite_version)
    else:
        # SQLite was compiled with SQLITE_THREADSAFE=1 or 2
        if _sqlite3.sqlite_threadsafe() == 0:
            raise sqlite3.ProgrammingError("SQLite was not compiled with "
                                           "threading support (found %s)." %
                                           _sqlite3.sqlite_version)

def _assert_synchronous():
    """
    Check that sqlite3 was compiled
