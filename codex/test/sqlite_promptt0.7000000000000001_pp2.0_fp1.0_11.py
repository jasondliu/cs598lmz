import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# http://www.sqlite.org/threadsafe.html
# SQLite is threadsafe but not in the sense of threadsafe
# like a Python list.  The library is threadsafe so that
# two threads can safely make calls into the same connection
# at the same time. Indeed, the SQLite library is designed so
# that two or more threads can use SQLite on the same database
# concurrently, with the library taking care of any necessary
# locking to avoid corruption of the database.

# http://docs.python.org/library/ctypes.html#ctypes.util.find_library
# ctypes.util.find_library(name)
# Search the default library search path for the library name
# and return a pathname. If no library can be found, returns None.

# ctypes.CDLL(name, mode=0, handle=None, use_errno=False,
#             use_last_error=False)
# Load the shared library name, using the ctypes.find_library()
# function. If use_errno is True, then if the function
