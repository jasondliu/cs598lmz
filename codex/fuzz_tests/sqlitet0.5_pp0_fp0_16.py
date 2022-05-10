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
    del my_threading_local.a
    return 1

def my_cb_auth(p):
    return 1

def my_cb_profile(p):
    return 1

def my_cb_trace(p):
    return 1

def my_cb_progress(p):
    return 1

def my_cb_commit(p):
    return 1

def my_cb_rollback(p):
    return 1

def my_cb_update(p):
    return 1

def my_cb_wal(p):
    return 1

def my_cb_busy(p):
    return 1

def my_cb_row(p):
    return 1

def my_cb_finalize(p):
    return 1

def my_cb_interrupt(p):
    return 1

def my_cb_trace_v2(p):
    return 1

def my_cb_profile_v2(p):
    return 1

def my_cb_wal_
