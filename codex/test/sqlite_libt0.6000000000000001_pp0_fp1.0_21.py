import ctypes
import ctypes.util
import threading
import sqlite3
import os

# Find and load the libsqlite3 library.
#
# This is a bit tricky, because the library may be in different places depending
# on the platform and how it was installed.  We try to follow the convention
# used by the sqlite3 module from the Python standard library.  We look for
# the library in the following locations:
#
# * ctypes.util.find_library('sqlite3')
# * ctypes.util.find_library('libsqlite3.so')
# * ctypes.util.find_library('libsqlite3.dylib')
# * ctypes.util.find_library('libsqlite3.dll')
#
_sqlite3 = None
for _name in ('sqlite3', 'libsqlite3.so', 'libsqlite3.dylib', 'libsqlite3.dll'):
    _libname = ctypes.util.find_library(_name)
