import ctypes
import ctypes.util
import threading
import sqlite3

lock = threading.RLock()

# Define ctypes for all the relevant functions.
# dlopen and dlsym
libdl = ctypes.CDLL(ctypes.util.find_library('dl'))
c_dlopen = libdl.dlopen
c_dlopen.argtypes = [ctypes.c_char_p, ctypes.c_int]
c_dlopen.restype = ctypes.c_void_p
c_dlsym = libdl.dlsym
c_dlsym.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
c_dlsym.restype = ctypes.c_void_p

# sqlite3_open, sqlite3_prepare_v2, sqlite3_finalize
libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
c_sqlite3_open = libsqlite3.sqlite3_open
