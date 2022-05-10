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

def my_step(p, *args):
    my_threading_local.a.execute("SELECT test(?, ?)", args)
    return 0

def my_final(p):
    return 0

def my_destroy(p):
    return

def my_value(p):
    return 0

def my_aggregate(p):
    return 0

def my_xstep(p, *args):
    my_threading_local.a.execute("SELECT test(?, ?)", args)
    return 0

def my_xfinal(p):
    return 0

def my_xdestroy(p):
    return

def my_xvalue(p):
    return 0

def my_xaggregate(p):
    return 0

def my_xstep_by_name(p, *args):
    my_threading_local.a.execute("SELECT test(?, ?)", args)
    return 0

def my_xfinal_by_name(p):
    return 0

def my_xdestroy_by_name(
