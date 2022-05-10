import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.create_aggregate()

# Issue #9840: create_aggregate() should return the aggregate object
# and not a SQLite function object.

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_create_function_v2.restype = ctypes.c_int
lib.sqlite3_create_function_v2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

lib.sqlite3_create_aggregate.restype = ctypes.c_int
lib.sqlite3_create_aggregate.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p,
