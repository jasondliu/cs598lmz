import ctypes
import ctypes.util
import threading
import sqlite3

# Enable the multithreaded SQLite3 module
if not sqlite3.threadsafety:
    raise RuntimeError("SQLite3 has not been compiled with a multithreaded flag")

# Load the SQLite3 DLL
try:
    sqlite3.sqlite_version
except AttributeError:
    sqlite3_lib = ctypes.util.find_library('sqlite3')
else:
    sqlite3_lib = None

if sqlite3_lib:
    _sqlite3 = ctypes.CDLL(sqlite3_lib)
else:
    # If we can't find the sqlite3 library, then use the fallback
    # location. This is useful on systems like Debian, where the
    # actual library is installed in a subdirectory.
    _sqlite3 = ctypes.CDLL('libsqlite3.so.0')

# Make sure that the threading flag is enabled
if not hasattr(_sqlite3, 'sqlite3_config'):
    raise RuntimeError("The sqlite3 module was compiled without support for external threads")

