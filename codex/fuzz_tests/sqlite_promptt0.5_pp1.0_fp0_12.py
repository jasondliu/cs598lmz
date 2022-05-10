import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb?mode=memory&cache=shared')

# We use sqlite3_open_v2() with SQLITE_OPEN_SHAREDCACHE.
# This means that we must use sqlite3_enable_shared_cache().
if not hasattr(sqlite3, 'enable_shared_cache'):
    raise ImportError('sqlite3 module does not have the enable_shared_cache attribute')

# This is the default value of the SQLITE_THREADSAFE compile-time option.
# It should be 1 (single-thread) or 2 (multi-thread).
# If it is 0, then the SQLite library is not threadsafe and should not be used.
sqlite3_threadsafe = sqlite3.threadsafety

# We need to use sqlite3_config() to set the SQLITE_CONFIG_MULTITHREAD option.
# We try to find the sqlite3_config() function in the sqlite3 library.
# We have to use ctypes.cdll.LoadLibrary() instead of ctypes.CDLL() because we
# need to load the
