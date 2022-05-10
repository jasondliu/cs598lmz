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
    return 1

def my_cb3(p):
    ret = my_threading_local.a.execute("SELECT test(1, 2)").fetchone()[0]
    if ret != 1:
        raise Exception("test_fn not called")
    return 1

def my_cb4(p):
    return 1

def my_cb5(p):
    return 1

def test_cb(cb, cb2, cb3, cb4, cb5):
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)
    lib.sqlite3_config(3, cb, 0)
    lib.sqlite3_config(4, cb2, 0)
    lib.sqlite3_config(5, cb3, 0)
    lib.sqlite3_config(6, cb4, 0)
    lib.sqlite3_config(7, cb5,
