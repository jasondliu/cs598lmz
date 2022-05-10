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

class Test(unittest.TestCase):
    def test_cb(self):
        my_cb(None)
        self.failUnless(hasattr(my_threading_local, 'a'))
        self.failUnless(my_threading_local.a.execute("select test(4, 5)").fetchone()[0] == 4)

if __name__ == '__main__':
    unittest.main()
