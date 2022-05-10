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

def my_cb_close(p):
    my_threading_local.a.close()
    del my_threading_local.a
    return 1

def my_cb_final(p):
    my_threading_local.a.close()
    del my_threading_local.a
    return 1

def my_cb_auth(p, a, b, c, d):
    return 1

def my_cb_trace(p, a):
    return 1

def my_cb_profile(p, a, b):
    return 1

def my_cb_progress(p):
    return 1

def my_cb_update(p, a, b, c, d):
    return 1

def my_cb_commit(p):
    return 1

def my_cb_rollback(p):
    return 1

def my_cb_wal_hook(p, a, b):
    return 1

def my_cb_vfs_find(p, a):
    return 1

def my_cb_v
