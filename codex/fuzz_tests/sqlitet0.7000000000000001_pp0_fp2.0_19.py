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

def my_cb_error(x, y):
    print("my_cb_error called")

def my_cb_trace(x, y):
    print("my_cb_trace called")

def my_cb_profile(x, y):
    print("my_cb_profile called")

def my_cb_authorize(x, y, z):
    print("my_cb_authorize called")

def my_cb_commit_hook(x):
    print("my_cb_commit_hook called")

def my_cb_rollback_hook(x):
    print("my_cb_rollback_hook called")

def my_cb_update_hook(x, y, z, a):
    print("my_cb_update_hook called")

def my_cb_collation(x, y):
    print("my_cb_collation called")

def my_cb_progress(x):
    print("my_cb_progress called")

def my_cb_busy(x):
    print("my_cb_bus
