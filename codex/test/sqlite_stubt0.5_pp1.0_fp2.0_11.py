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
    my_threading_local.a.close()

    return 1

def my_cb3(p):
    a = my_threading_local.a

    if a is None:
        return 0

    return 1

def my_cb4(p):
    return my_threading_local.a.cursor().execute("SELECT test(1, 2)").fetchone()[0]

def my_cb5(p):
    return my_threading_local.a.cursor().execute("SELECT test(1, 2)").fetchone()[0]

def main():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_enable_shared_cache(0)

    lib = ctypes.CDLL("libsqlitefunctions.so")

    lib.sqlite3_test_init()

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
