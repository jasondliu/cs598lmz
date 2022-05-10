import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def get_sqlite3_version():
    # Get sqlite3 version
    sqlite3_version = sqlite3.sqlite_version
    print("sqlite3 version: %s" % sqlite3_version)
    return sqlite3_version

def get_sqlite3_version_from_lib():
    # Get sqlite3 version from lib
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_libversion.restype = ctypes.c_char_p
    sqlite3_version = lib.sqlite3_libversion()
    print("sqlite3 version: %s" % sqlite3_version)
    return sqlite3_version

def get_sqlite3_version_from_lib_with_thread():
    # Get sqlite3 version from lib with thread
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_libversion.restype = ctypes.c_char_p
