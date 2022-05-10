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
    if hasattr(my_threading_local, "a"):
        my_threading_local.a.close()
        del my_threading_local.a

    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_set_authorizer.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
lib.sqlite3_set_authorizer.restype = None
lib.sqlite3_set_authorizer(None, my_cb, None)
lib.sqlite3_set_authorizer(None, my_cb2, None)

class Test(unittest.TestCase):
    def test_1(self):
        a = sqlite3.connect(DB_URI, uri=True)
        a.execute("create table test (a)")
        a.execute("insert into test values (test(1, 2))")
