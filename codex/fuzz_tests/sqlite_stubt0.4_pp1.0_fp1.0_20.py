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
    a.execute("select test(?, ?)", (1, 2))
    return 1

def my_cb3(p):
    a = my_threading_local.a
    a.execute("select test(?, ?)", (1, 2))
    a.close()
    return 1

def my_cb4(p):
    a = my_threading_local.a
    a.execute("select test(?, ?)", (1, 2))
    a.close()
    return 1

def my_cb5(p):
    a = my_threading_local.a
    a.execute("select test(?, ?)", (1, 2))
    a.close()
    return 1

def my_cb6(p):
    a = my_threading_local.a
    a.execute("select test(?, ?)", (1, 2))
    a.close()
    return 1

def my_cb7(p):
    a = my_
