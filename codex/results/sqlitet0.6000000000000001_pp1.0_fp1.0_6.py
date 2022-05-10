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
    a = my_threading_local.a

    a.execute("create table test (id int)")
    a.execute("insert into test values (test(1, 2))")

    return 1

def my_cb3(p):
    a = my_threading_local.a

    a.execute("select test(1, 2)")

    return 1

def my_cb4(p):
    a = my_threading_local.a

    # this is the function that causes the crash
    a.execute("select * from test")

    return 1

def register_callbacks(db):
    cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    cb_ptr = cb_type(my_cb)
    db.sqlite3_trace_v2(db, 0, cb_ptr, None)
    cb_ptr = cb_type(my_cb2)
    db.sqlite3_trace_
