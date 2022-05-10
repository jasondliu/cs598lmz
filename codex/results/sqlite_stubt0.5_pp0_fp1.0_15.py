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

def my_err_cb(p):
    my_threading_local.a = None
    return 1

def my_commit_cb(p):
    if my_threading_local.a is not None:
        my_threading_local.a.commit()
    return 1

def my_rollback_cb(p):
    if my_threading_local.a is not None:
        my_threading_local.a.rollback()
    return 1

def my_update_cb(p, typ, db, tbl, rowid):
    if my_threading_local.a is not None:
        my_threading_local.a.execute("INSERT INTO sqlite_master VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (typ, db, tbl, rowid, "", "", "", "", ""))
    return 1

def my_authorize_cb(p, typ, arg1, arg2, db, tbl):
    if my_threading_local.a is not None:
