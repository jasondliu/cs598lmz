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

def a():
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    b.create_function("test", 2, lambda x: x)

    my_threading_local.b = b

    return 1

def b():
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    c.create_function("test", 2, lambda x: x)

    my_threading_local.c = c

    return 1

if __name__ == '__main__':
    expected_result = [1] * 3

    sqlite3.sqlite3_api_routines.sqlite3_shutdown.restype = ctypes.c_int
    sqlite3.sqlite3_api_routines.sqlite3_config.restype = ctypes.c_int
    sqlite3.sqlite3_api_routines.sqlite3_config(
        sqlite3.SQLITE_CONFIG_MULTITHREAD,
