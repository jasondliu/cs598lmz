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

def test_cb(p):
    return 1

def main():
    ctypes.CDLL(ctypes.util.find_library("sqlite3"), ctypes.RTLD_GLOBAL)
    sqlite3.sqlite_open_v2(":memory:", 0, None)
    sqlite3.sqlite3_create_function_v2(my_threading_local.a.connection_pointer, b"test", 2, 1, None, test_cb, None, None, None)

if __name__ == "__main__":
    main()
