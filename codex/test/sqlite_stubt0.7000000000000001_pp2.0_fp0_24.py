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

class TestUserFunctions(unittest.TestCase):
    def setUp(self):
        self.p = pysqlcipher.sqlite3_open(":memory:", "")
        self.p.set_authorizer(my_cb)
        assert self.p.get_autocommit() == 1
        self.p.close()

    def tearDown(self):
        pass

    def test_user_functions_in_threads(self):
        def test_thread():
            a = my_threading_local.a
            assert a is not None
            cursor = a.cursor()
            cursor.execute("select test(?, ?)", (1, 2))
            row = cursor.fetchone()
            assert row[0] == 1

        t1 = threading.Thread(target=test_thread)
        t2 = threading.Thread(target=test_thread)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

