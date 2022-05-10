import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# from https://github.com/python/cpython/blob/master/Modules/_sqlite/cursor.c
# and https://github.com/python/cpython/blob/master/Modules/_sqlite/connection.c
# and https://github.com/python/cpython/blob/master/Modules/_sqlite/microprotocols.c

# https://docs.python.org/3/library/ctypes.html
# https://docs.python.org/3/library/ctypes.html#ctypes.c_int.from_address
# https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p.from_address
# https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p.value
# https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p.__int__
# https://docs.python.org/3/
