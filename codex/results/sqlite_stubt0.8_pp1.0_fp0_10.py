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
    a.execute("select test('hello', 'world')")
    return 1

def my_cb3(p):
    a = my_threading_local.a
    a.close()
    del my_threading_local.a
    return 1

class MyTest(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class MyTest2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_float),
                ("b", ctypes.c_float),
                ("c", ctypes.c_float),
                ("d", ctypes.c_float)]

class TestFts(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
       
