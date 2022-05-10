import ctypes
import ctypes.util
import threading
import sqlite3
import struct
import array
import psutil

from contextlib import closing


# ctypes types and ctypes.util.find_library

_c_bool = ctypes.c_byte
_c_ssize_t = ctypes.c_long
_c_size_t = ctypes.c_ulong

_c_int = ctypes.c_int
_c_uint = ctypes.c_uint
_c_long = ctypes.c_int
_c_ulong = ctypes.c_uint

_c_ulong64 = ctypes.c_ulonglong  # FIXME: Use the correct type (not avaialbale on Python 2.4)

_c_char_p = ctypes.c_char_p
# Note, sqlite3 ships a libsqlite3.dll which is not usable with ctypes.
sqlite3_libname = ctypes.util.find_library('sqlite3')
if sqlite3_libname is None:
    sqlite3_libname = ctypes.util.find_library('sql
