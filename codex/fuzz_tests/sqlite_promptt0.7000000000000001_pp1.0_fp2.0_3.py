import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
from _sqlite3 import *

from . import util
from . import _sqlite3
from .dbapi2 import *

version_info = (3, 8, 1, "")
sqlite_version_info = (3, 8, 1)

# Threading and sharing support.

def enable_shared_cache(do_enable):
    """Enable or disable shared cache mode for the calling thread.

    Shared cache is disabled by default.
    """
    if do_enable:
        _sqlite3.sqlite3_enable_shared_cache(1)
    else:
        _sqlite3.sqlite3_enable_shared_cache(0)


def complete_statement(sql):
    """Attempts to complete the given SQLite statement.

    Returns True if the string is complete (as far as sqlite3 is concerned),
    or False if it is incomplete (sqlite3 expects more tokens).
    """
    return _sqlite3.sqlite3_complete(sql)


def complete_error_message():
    """Returns an error message if the
