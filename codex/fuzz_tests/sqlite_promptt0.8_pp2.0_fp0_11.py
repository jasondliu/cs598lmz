import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect in thread
import _sqlite3

# ctypes.util.find_library('sqlite3')
# _sqlite3.sqlite_version_info
print dir(_sqlite3)
print ctypes.util.find_library('sqlite3')

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
print lib
print lib._name
# from ctypes import *
# lib = cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
# lib = cdll.LoadLibrary('libsqlite3.so')

# print lib
# print dir(lib)
# print lib.sqlite_version
# for i in dir(lib):
#     print i

# print lib.sqlite3_libversion
# print lib.sqlite3_libversion_number
# print lib.sqlite3_changes
# print lib.sqlite3_errcode
# print lib.sqlite3_errmsg
# print lib.sqlite3_memory_used
# print lib.sqlite3_memory
