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
    try:
        conn = my_threading_local.a
        conn.cursor().execute("select test(1, 2)")
    except:
        pass

    return 1

def my_cb3(p):
    try:
        conn = my_threading_local.a
        conn.close()
    except:
        pass

    return 1

def my_cb4(p):
    try:
        conn = my_threading_local.a
        conn.cursor().execute("select test(1, 2)")
    except:
        pass

    return 1

def my_cb5(p):
    try:
        conn = my_threading_local.a
        conn.close()
    except:
        pass

    return 1

def my_cb6(p):
    try:
        conn = my_threading_local.a
        conn.cursor().execute("select test(1, 2)")
    except:
        pass

    return 1

def my_cb7
