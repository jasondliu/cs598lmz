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

def my_cb_2(p, a, b):
    return my_threading_local.a.execute("SELECT test(?, ?)", (a, b)).fetchone()[0]

def my_cb_3(p, a, b):
    return my_threading_local.a.execute("SELECT test(?, ?)", (a, b)).fetchone()[0]

def test_threads():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_create_function_v2(
        my_threading_local.a.dbapi_connection.connection,
        b"test_threads", 2, 1, None, my_cb, my_cb_2, None, None
    )

