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

class SQLiteThreadingTests(unittest.TestCase):
    def setUp(self):
        self.dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        self.dll.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
        self.dll.sqlite3_open.restype = ctypes.c_int
        self.dll.sqlite3_close.argtypes = [ctypes.c_void_p]
        self.dll.sqlite3_close.restype = ctypes.c_int

    def test_threading(self):
        from sqlite3 import apilevel
        self.assertEqual(apilevel, '2.0')
        self.dll.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p()))
        self.dll.sqlite3_close(ctypes.c_void_p())

    def test_threading
