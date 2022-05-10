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

def my_cb2(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def test_callback(sqlite_api):
    sqlite_api.sqlite3_shutdown()
    sqlite_api.sqlite3_config(sqlite_api.SQLITE_CONFIG_URI, 1)
    sqlite_api.sqlite3_initialize()

    sqlite_api.sqlite3_enable_load_extension(my_threading_local.a, 1)
    sqlite_api.sqlite3_load_extension(my_threading_local.a, "./extension-functions.so", "test_callback", None)

    sqlite_api.sqlite3_enable_load_extension(my_threading_local.a, 0)

    sql
