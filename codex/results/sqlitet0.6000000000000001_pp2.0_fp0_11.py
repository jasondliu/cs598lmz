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
    def test_connect(self):
        my_cb(None)

        a = my_threading_local.a

        # check the connection object is not deleted
        self.assertEqual(a.execute('select test(1, 2)').fetchone()[0], 1)

        del my_threading_local.a
        my_threading_local.a = None

        lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
        lib.malloc(1)
        lib.free(1)

if __name__ == "__main__":
    unittest.main()
