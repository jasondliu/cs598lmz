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

def my_cb_2(p):
    my_threading_local.a.close()
    return 1

def my_cb_3(p):
    return 1

def my_cb_4(p):
    return 1

def test_f():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    sqlite3.set_authorizer(my_cb_2)
    sqlite3.set_authorizer(my_cb_3)
    sqlite3.set_authorizer(my_cb_4)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("create table a (x int)")

    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b.execute("select test(x, 1) from a")

def test_l():
    test_f()
    return False

if __name__ == "
