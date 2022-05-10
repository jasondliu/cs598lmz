import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";
# conn.close()

# Test ctypes.util.find_library()
# print ctypes.util.find_library('sqlite3')

# Test ctypes.CDLL()
# lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
# print lib

# Test ctypes.c_char_p()
# lib.sqlite3_libversion.restype = ctypes.c_char_p
# print lib.sqlite3_libversion()

# Test ctypes.c_int()
# lib.sqlite3_libversion_number.restype = ctypes.c_int
# print lib.sqlite3_libversion_number()

# Test ctypes.c_int()
# lib.sqlite3_threadsafe.restype = ctypes.c_int
# print lib.sqlite3_threadsafe()

# Test ctypes.c_int()
# lib.sqlite3_open.
