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

def my_test(uri):
    if uri:
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    else:
        a = sqlite3.connect(":memory:")
        a.execute("create virtual table test using fts4(x)")
        a.commit()

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    if uri:
        ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open_v2(
            DB_URI, ctypes.c_void_p(), 1, None
        )
    else:
        ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open_v2(
            ":memory:", ctypes.c_void_p(), 1, None
        )

    return 1

def main():
    test_
