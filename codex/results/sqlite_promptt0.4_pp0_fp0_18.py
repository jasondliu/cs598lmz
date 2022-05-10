import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# TODO:
#  - add a "shutdown" method to the class
#  - add a "fork" method to the class


# The following code is based on the Python 3.5.2 source code.
# https://github.com/python/cpython/blob/3.5/Modules/_sqlite/cursor.c#L204-L210
# https://github.com/python/cpython/blob/3.5/Modules/_sqlite/connection.c#L1158-L1162
# https://github.com/python/cpython/blob/3.5/Modules/_sqlite/connection.c#L1164-L1169

# The _sqlite3.Connection class is a wrapper around the sqlite3_connection
# struct.  The sqlite3_connection struct has a sqlite3* field, and the
# sqlite3* is a pointer to the sqlite3 struct.  The sqlite3 struct has a
# void* field named "pVfs".
