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
    return 1

def my_cb_test(p):
    return my_threading_local.a.execute("select test(1, 2)").fetchone()[0]

def my_cb_test_err(p):
    return my_threading_local.a.execute("select test(1, 2, 3)").fetchone()[0]

def my_cb_test_err2(p):
    return my_threading_local.a.execute("select test(1, 2)").fetchone()[0]

def my_cb_test_err3(p):
    return my_threading_local.a.execute("select test(1, 2)").fetchone()[0]

def my_cb_test_err4(p):
    return my_threading_local.a.execute("select test(1, 2)").fetchone()[0]

def my_cb_test_err5(p):
