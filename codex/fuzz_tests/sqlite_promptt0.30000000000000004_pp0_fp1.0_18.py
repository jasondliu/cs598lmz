import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

from . import _sqlite3

# Threading check
if _sqlite3.sqlite_version_info < (3, 6, 8):
    raise ImportError("sqlite3.threadsafety is 2 but sqlite3 version is %d.%d.%d" % _sqlite3.sqlite_version_info)

# Check for sqlite3_open_v2
if not hasattr(_sqlite3, 'sqlite3_open_v2'):
    raise ImportError("sqlite3.sqlite3_open_v2 is not available")

# Check for sqlite3_errstr
if not hasattr(_sqlite3, 'sqlite3_errstr'):
    raise ImportError("sqlite3.sqlite3_errstr is not available")

# Check for sqlite3_enable_load_extension
if not hasattr(_sqlite3, 'sqlite3_enable_load_extension'):
    raise ImportError("sqlite3.sqlite3_enable_load_extension is not available")

# Check
