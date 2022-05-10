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
    def setUp(self):
        test_lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        test_lib.sqlite3_enable_shared_cache(1)
        self.thread_one = threading.Thread(target=my_cb, args=(1,))
        self.thread_one.start()
        self.thread_one.join()

    def tearDown(self):
        pass

    def test_db_is_none(self):
        self.assertIsNone(my_threading_local.a.test(1, 2))


if __name__ == '__main__':
    unittest.main()
