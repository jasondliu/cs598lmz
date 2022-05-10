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
    b = my_threading_local.a

    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    z = b.cursor()
    z.execute("select test(?);", [1])
    z = z.fetchall()

    z = c.cursor()
    z.execute("select test(?);", [1])
    z = z.fetchall()

    my_threading_local.a = c

    return 1

def main():
    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    dll.sqlite3_enable_shared_cache(1)
    dll.sqlite3_config(5, 1)
    dll.sqlite3_config(7, ctypes.cast(ctypes.pythonapi.Py_DecRef, ctypes.c_void_p))

    db = sqlite3.connect(DB_URI, uri=True, factory=dele
