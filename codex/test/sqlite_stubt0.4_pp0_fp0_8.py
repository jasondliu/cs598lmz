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

def my_busy_cb(p):
    return 1

def my_trace_cb(p, sql):
    print(sql)
    return 1

def my_progress_cb(p):
    return 1

def my_commit_cb(p):
    return 1

def my_rollback_cb(p):
    return 1

def my_update_cb(p, op, db, tbl, rowid):
    return 1

def my_authorize_cb(p, op, arg1, arg2, db, tbl):
    return 1

def my_wal_cb(p, db, name):
    return 1

def my_profile_cb(p, sql, tm):
    print(sql, tm)
    return 1

def my_coll_cb(p, s1, s2):
    return 1

def my_func_cb(p, n, vals):
    return 1

def my_step_cb(p, n, vals):
    return 1

