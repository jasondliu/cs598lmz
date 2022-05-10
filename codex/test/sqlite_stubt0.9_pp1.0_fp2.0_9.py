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


r = ctypes.CDLL(ctypes.util.find_library("re2"))
r.RE2_NewWrapper.argtypes = [ctypes.c_char_p, ctypes.c_int]
r.RE2_NewWrapper.restype = ctypes.c_void_p

query_str = "SELECT test('foo', 'bar')"

conditions = []

