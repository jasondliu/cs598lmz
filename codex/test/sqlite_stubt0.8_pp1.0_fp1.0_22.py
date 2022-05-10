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

def test_my_threading_local():
    my_threading_local.a = 0
    assert my_threading_local.a == 0

    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    dll.sqlite3_config(2, 1)
    dll.sqlite3_enable_shared_cache(1)

    cb = sqlite3.SQLITE_INTEGER(my_cb)

    dll.sqlite3_initialize()

    dll.sqlite3_shutdown()

    assert my_threading_local.a == 0
