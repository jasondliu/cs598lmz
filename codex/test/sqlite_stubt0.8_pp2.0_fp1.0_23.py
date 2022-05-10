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
    sqlite_path = ctypes.util.find_library("sqlite3")
    if sqlite_path is None:
        raise Exception("sqlite3 not found")

    sqlite3 = ctypes.CDLL(sqlite_path)

    sqlite3.sqlite3_enable_shared_cache(1)

    sqlite3.sqlite3_initialize()
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
    sqlite3.sqlite3_enable_load_extension(1)
    sqlite3.sqlite3_enable_shared_cache(1)
    sqlite3.sqlite3_open(DB_URI, ctypes.pointer(p))

    sqlite3.sqlite3_create_function_v2(p, b"my_cb", 0, sqlite3.SQLITE_UTF8, None, my_cb, None, None, None)
