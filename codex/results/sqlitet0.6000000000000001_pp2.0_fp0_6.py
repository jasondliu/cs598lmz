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

def my_cb_del(p):
    del my_threading_local.a
    return 1

def my_cb_fetch(p):
    return my_threading_local.a.execute("SELECT test(1, 2)").fetchone()[0]

def my_cb_commit(p):
    my_threading_local.a.commit()
    return 1

def my_cb_rollback(p):
    my_threading_local.a.rollback()
    return 1

def my_cb_close(p):
    my_threading_local.a.close()
    return 1

def my_cb_reopen(p):
    my_threading_local.a = sqlite3.connect(DB_URI, uri=True)
    return 1

def my_cb_convert_text(p):
    return my_threading_local.a.execute("SELECT CAST(1 AS TEXT)").fetchone()[0]

def my_cb_fetch_all(p):
   
