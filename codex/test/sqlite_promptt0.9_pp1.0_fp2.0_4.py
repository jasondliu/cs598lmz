import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection(False, 1)

mh = ctypes.CDLL(ctypes.util.find_library("m"))
malloc = mh.malloc
mh.malloc.restype = ctypes.c_void_p
free = mh.free

idle_cur = None
idle_con = None

libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int]
libsqlite3.sqlite3_open_v2.restype = ctypes.c_int
libsqlite3.sqlite3_prepare_v2.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
libsqlite3.sqlite3_prepare_v2.restype = ctypes
