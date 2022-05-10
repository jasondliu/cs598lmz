import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(:memory:) with multiple threads.
# ctypes is used to access sqlite_enable_shared_cache().

def main():
    # Find the sqlite3 library
    libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    # Look for sqlite3_enable_shared_cache function
    try:
        libsqlite3.sqlite3_enable_shared_cache
    except AttributeError:
        print("library does not have shared cache api")
        libsqlite3 = None
    else:
        # Try to enable shared cache mode
        if libsqlite3.sqlite3_enable_shared_cache(1) != 1:
            print("failure to enable shared cache mode")
            libsqlite3 = None
        else:
            print("enabled sqlite shared cache mode")
    failures = set()
    def test(create_db_func, name):
        global failures, libsqlite3
        try:
            create_db_func(None)
        except Exception as e:
            print("
