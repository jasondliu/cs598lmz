import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory', uri=1)
try:
    import thread
except ImportError:
    import _thread as thread

from . import util
from . import dbapi2

# NOTE: REMOVE THIS ONCE CODE IS RELEASED
import pytest

# NOTE: This is an experiment, I would like to see if we can use an
# introspected enum which is accessible by our C code.
libpysqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

try:
    SQLITE_OPEN_URI = 0x10
except AttributeError:
    SQLITE_OPEN_URI = 0x08  # Old value

# Specify SQLite3 extension libraries to load, these must be present on
# the filesystem and be loadable from the SQLite load_extension()
# method.
#
# NOTE: The "json1" extension is only available in SQLite 3.9.0+.
#
# NOTE: The "rtree" extension is only available in SQLite 3.8.0+.
#
# NOTE:
