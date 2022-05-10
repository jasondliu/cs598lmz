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

def my_cb_final(p):
    my_threading_local.a.close()

    return 1

def my_cb_step(p, n, a, b, c, d):
    return 1

def my_cb_func(p, n, a):
    return 1

def my_cb_trace(p, a):
    return 1

def my_cb_profile(p, a, b):
    return 1

def my_cb_progress(p):
    return 1

def my_cb_commit(p):
    return 1

def my_cb_rollback(p):
    return 1

def my_cb_update(p, a, b, c, d, e):
    return 1

def my_cb_authorize(p, a, b, c, d, e):
    return 1

def my_cb_row(p, a):
    return 1

def my_cb_finalize(p):
    return 1

def my_cb_busy(p, a):
    return
