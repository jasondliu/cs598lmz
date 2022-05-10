import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect first, because the error message is not very helpful
# otherwise.
sqlite3.connect(':memory:').close()

# Add the location of the library to the path.
# NOTE: this is brittle and will fail if the user changes the working directory.
ctypes.CDLL(os.path.join(os.getcwd(), 'libs_and_wrappers/lib/libsqlite3.so'))

# Load the library, using either the fully specified filename or whatever
# ctypes.util.find_library returns.
sqlite_lib = ctypes.CDLL('libsqlite3.so')
if sqlite_lib is None:
    sqlite_lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
if sqlite_lib is None:
    raise ImportError('Could not load the sqlite3 library.')

# int sqlite3_open(
#   const char *filename,   /* Database filename (UTF-8) */
#   sqlite3 **ppDb          /* OUT: SQLite db handle */
# );
sqlite
