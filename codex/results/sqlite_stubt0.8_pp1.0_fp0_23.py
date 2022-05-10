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

class MyTest(unittest.TestCase):
    def test_thread_local(self):
        libc = ctypes.CDLL(ctypes.util.find_library('c'))

        self.assertRaises(AttributeError, getattr, my_threading_local, 'a')

        libc.pthread_create(ctypes.c_void_p(), ctypes.c_void_p(), ctypes.c_void_p(my_cb), None)
        self.assertTrue(my_threading_local.a)

        self.assertRaises(AttributeError, getattr, my_threading_local, 'a')

if __name__ == '__main__':
    unittest.main()
