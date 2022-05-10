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

if __name__ == "__main__":
    sqlite3.sqlite3_initialize()

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)

    sqlite3.sqlite3_enable_shared_cache(1)

    sqlite3.sqlite3_auto_extension(ctypes.pythonapi.PyCapsule_New.restype(None)(ctypes.util.find_library("sqlite3"), None, None))

    sqlite3.sqlite3_enable_load_extension(0)

    sqlite3.sqlite3_enable_load_extension(1)

    sqlite3.sqlite3_enable_load_extension(0)

    sqlite3.sqlite3_enable_load_extension(1)

    sqlite3.sqlite3_auto_extension(ctypes.pythonapi.PyCapsule_New.restype(None)(ctypes.util.find_library("sqlite3"), None, None))

    sqlite3.sqlite3
