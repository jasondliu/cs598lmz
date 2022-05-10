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
# https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p.value
# https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p.in_dll
# https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p.from_address
# https://docs.python.org/3/library/ctypes.html
