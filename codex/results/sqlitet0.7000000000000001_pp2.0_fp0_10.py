import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def test_threading():
    # Load the sqlite extension module
    dll = ctypes.util.find_library("sqlite3")
    if not dll:
        raise Exception("sqlite3 library not found")
    sqlite3 = ctypes.CDLL(dll)

    # Enable extension loading
    sqlite3.sqlite3_enable_load_extension(None, 1)

    sqlite3.sqlite3_config(ctypes.c_int(45), ctypes.c_int(1))
    sqlite3.sqlite3_config(ctypes.c_int(7), ctypes.c_int(1))
    sqlite3.sqlite3_initialize()

    # Register the custom callback
    sqlite3.sqlite3_auto_extension(my_cb)

    # Load the custom extension
    sqlite3.sqlite3_load_extension(None, "test", None)

    sqlite3.sqlite3_shutdown()

    conn = my_threading_local.a
    result = conn.execute
