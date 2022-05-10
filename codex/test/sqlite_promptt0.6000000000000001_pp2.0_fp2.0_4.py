import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect(None)

# Test the behaviour of the sqlite3 module when the library can not be
# loaded.
#
# To test this we first try to load a non-existent library.  This should
# fail and cause an ImportError to be raised.
#
# Next we try to load the real sqlite library.  This should succeed.
#
# Then we again try to load the non-existent library and this should fail
# without raising an exception.

lib = ctypes.util.find_library('this_library_does_not_exist')
if not lib:
    raise ImportError('could not find a non-existent library')

try:
    ctypes.CDLL(lib)
except OSError:
    pass
else:
    raise ImportError(
        'loading a non-existent library succeeded unexpectedly')

lib = ctypes.util.find_library('sqlite3')
if not lib:
    raise ImportError('could not find the sqlite3 library')
