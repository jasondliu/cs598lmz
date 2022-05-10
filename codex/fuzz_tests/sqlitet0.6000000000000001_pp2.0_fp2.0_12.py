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

def my_callback_factory(p, n_col, col_value, col_name):
    def my_callback(p, n_col, col_value, col_name):
        print("callback")
        return 0
    return my_callback

class MyError(Exception):
    pass

def test_fn(a, b):
    return a

def my_progress(p):
    print("progress")
    return 0

def my_progress_handler(p):
    print("progress handler")
    return 0

def my_busy_handler(p, n):
    print("busy handler")
    return 0

def my_trace(p, sql):
    print("trace", sql)
    return 0

def my_authorizer(p, action, arg1, arg2, dbname, source):
    print("authorizer", action, arg1, arg2, dbname, source)
    return 0

def my_update_hook(p, op, db, tbl, rowid):
    print("update hook", op, db
