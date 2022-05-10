import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL
# https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p
# https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p
# https://docs.python.org/3/library/ctypes.html#ctypes.c_int
# https://docs.python.org/3/library/ctypes.html#ctypes.c_size_t

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_aggregate
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_collation
# https://docs.python.org/3/library/sqlite3.html
