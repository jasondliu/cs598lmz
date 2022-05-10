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
    a.execute("select test(4, 5)")

def my_cb3(p):
    a = my_threading_local.a
    a.execute("select test(6, 7)")

def my_cb4(p):
    a = my_threading_local.a
    a.execute("select test(8, 9)")

def my_cb5(p):
    a = my_threading_local.a
    a.execute("select test(10, 11)")
    del my_threading_local.a

def my_cb6(p):
    a = my_threading_local.a
    a.execute("select test(12, 13)")

def my_cb7(p):
    a = my_threading_local.a
    a.execute("select test(14, 15)")

def my_cb8(p):
    a = my_threading_local.a
    a.execute("
