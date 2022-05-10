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
    a = my_threading_local.a

    def test_fn(a, b):
        return b

    a.create_function("test", 2, test_fn)

    return 0

def main():
    check_sqlite3()

    try:
        dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
    except OSError:
        print("SKIP")
        raise SystemExit

    dll.sqlite3_initialize()

    p = ctypes.c_void_p()
    dll.sqlite3_open_v2(b"test", ctypes.byref(p),
        sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE, None)
    dll.sqlite3_create_function_v2(p, b"my_cb", -1, 0, None, my_cb, None, None, None)
    dll.sqlite
