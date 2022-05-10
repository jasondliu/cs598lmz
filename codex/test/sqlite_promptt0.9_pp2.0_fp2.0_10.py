import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.sql')

null = ctypes.POINTER(ctypes.c_int)()

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.malloc.restype = ctypes.c_char_p
libc.malloc.argtypes = [ctypes.c_size_t]
libc.getenv.restype = ctypes.c_char_p
libc.getenv.argtypes = [ctypes.c_char_p]
libc.setenv.restype = ctypes.c_int
libc.setenv.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
libc.unsetenv.restype = ctypes.c_int
libc.unsetenv.argtypes = [ctypes.c_char_p]

