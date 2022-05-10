import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect().
# c = sqlite3.connect("../databases/test.db")

# Get a handle to the library.
# lib = ctypes.cdll[ctypes.util.find_library("libsqlite3")]
# libsqlite3 = ctypes.CDLL('libsqlite3.so')
libsqlite3 = ctypes.CDLL('libsqlite3.so.0')
# libsqlite3 = ctypes.CDLL('/usr/lib/x86_64-linux-gnu/libsqlite3.so.0')
# libsqlite3 = ctypes.CDLL('/usr/lib/x86_64-linux-gnu/libsqlite3.so')
# libsqlite3 = ctypes.CDLL('/usr/lib/libsqlite3.so.0')
# libsqlite3 = ctypes.CDLL('/usr/lib/libsqlite3.so')

libsqlite3.sqlite3_libversion.restype = ctypes.c_char_p
libsqlite3.sqlite3_libversion.
