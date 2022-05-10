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
    del my_threading_local.a
    return 1

def test_threads():
    if not sqlite3.threadsafety:
        return

    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    callback = sqlite3.sqlite3_set_authorizer(dll, my_cb, None)
    callback2 = sqlite3.sqlite3_set_authorizer(dll, my_cb2, None)
    del callback
    del callback2
    c = sqlite3.connect(DB_URI, uri=True)
    c.execute("select test(1, 2)")
    c.close()

def test_threads_with_authorizer():
    if not sqlite3.threadsafety:
        return

    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
