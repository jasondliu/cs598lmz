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

def my_cb_finalize(p):
    my_threading_local.a.finalize()
    return 1

def my_cb_step(p):
    my_threading_local.a.execute("select test(1, 2)")
    return 1

def my_cb_reset(p):
    my_threading_local.a.execute("select test(1, 2)")
    my_threading_local.a.execute("select test(1, 2)")
    return 1

def my_cb_clear_bindings(p):
    my_threading_local.a.execute("select test(?, ?)", (1, 2))
    my_threading_local.a.execute("select test(?, ?)", (1, 2))
    return 1

def my_cb_column_name(p):
    my_threading_local.a.execute("select test(1, 2)")
    my_
