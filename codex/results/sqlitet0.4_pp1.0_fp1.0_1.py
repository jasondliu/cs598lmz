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

sqlite3.sqlite3_thread_cleanup()

sqlite3.sqlite3_thread_init()

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_thread_cleanup()

lib.sqlite3_config(1, my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

def f():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    a.execute("select test(1, 2)")

t = threading.Thread(target=f)
t.
