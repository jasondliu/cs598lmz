import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Test ctypes.util.find_library('sqlite3')

# Test ctypes.CDLL(ctypes.util.find_library('sqlite3'))

# Test ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_open(':memory:', ctypes.byref(ctypes.c_void_p()))

# Test ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_close(ctypes.c_void_p())

# Test ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_exec(ctypes.c_void_p(), 'create table t (id integer primary key, v text)', ctypes.c_void_p(), ctypes.c_void_p(), ctypes.c_void_p())

# Test ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_exec(ctypes.c_void_p(), '
