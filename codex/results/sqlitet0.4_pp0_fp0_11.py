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

    def test_fn2(a, b):
        return a

    a.create_function("test", 2, test_fn2)

    return 1

def test_thread_callback():
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.set_authorizer(my_cb)
    c.set_authorizer(my_cb2)
    c.execute("create table t(x)")
    c.execute("insert into t(x) values (test(?, ?))", (1, 2))
    c.execute("select test(?, ?) from t", (3, 4))

def test_thread_callback_2():
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.set_authorizer(my_cb)
    c.set_authorizer(my_cb2)
    c.execute("create table t(x
