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

def my_cb_trace(p, sql):
    print(sql)
    return 0

def my_cb_profile(p, sql, time):
    print(sql, time)
    return 0

def my_cb_progress(p):
    return 0

def my_cb_commit(p):
    return 0

def my_cb_rollback(p):
    return 0

def my_cb_update(p, op, db, tbl, rowid):
    return 0

def my_cb_authorize(p, op, arg1, arg2, db, tbl):
    return 0

def my_cb_row(p, ncols, values, names):
    return 0

def my_cb_complete(p, sql):
    return 0

def my_cb_busy(p, count):
    return 0

def my_cb_open(p, filename, mode):
    return 0
