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

class TestCase(unittest.TestCase):
    def setUp(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))
        self.libc.atexit.restype = ctypes.c_int
        self.libc.atexit.argtypes = [ctypes.CFUNCTYPE(None)]
        self.libc.atexit(ctypes.CFUNCTYPE(None)(my_cb))

    def tearDown(self):
        del my_threading_local.a

    def test_one(self):
        self.libc.exit(0)

if __name__ == '__main__':
    unittest.main()
