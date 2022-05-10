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
    my_threading_local.a.close()
    return 1

def my_cb3(p):
    my_threading_local.a = None
    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_test_control(1, my_cb)
lib.sqlite3_test_control(2, my_cb2)
lib.sqlite3_test_control(3, my_cb3)

lib.sqlite3_test_control(4)
lib.sqlite3_test_control(5)
lib.sqlite3_test_control(6)

lib.sqlite3_test_control(7)
lib.sqlite3_test_control(8)
lib.sqlite3_test_control(9)

lib.sqlite3_test_control(10)
lib.sqlite3_test_control(11)
lib.sqlite3_test_control(12)

lib.sqlite
