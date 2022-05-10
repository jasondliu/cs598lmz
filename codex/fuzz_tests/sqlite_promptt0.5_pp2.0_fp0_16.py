import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:test.db?mode=memory&cache=shared', uri=True)

# https://docs.python.org/3.3/library/sqlite3.html
# https://docs.python.org/3.3/library/sqlite3.html#sqlite3-threading

# https://docs.python.org/3/library/ctypes.html
# https://docs.python.org/3/library/ctypes.html#ctypes.CDLL
# https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p

# https://github.com/python/cpython/blob/3.3/Modules/_ctypes/callproc.c#L1511
# https://github.com/python/cpython/blob/3.3/Modules/_ctypes/callproc.c#L1524
# https://github.com/python/cpython/blob/3.3/Modules/_ctypes/callproc.c#L1527
# https://github.com/python/cpython
