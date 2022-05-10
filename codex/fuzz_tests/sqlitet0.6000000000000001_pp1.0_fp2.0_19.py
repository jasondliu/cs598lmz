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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_set_authorizer.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
lib.sqlite3_set_authorizer.restype = None
lib.sqlite3_set_authorizer(0, my_cb, 0)

class Test(unittest.TestCase):
    """
    This test doesn't crash.
    """

    def test_1(self):
        conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        conn.executemany("SELECT test(?, ?)", [(1, 2), (3, 4)])
        conn.close()

if __name__ == "__main__":
    unittest.main()
