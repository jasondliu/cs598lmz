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

class TestCreateFunction(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _open_a(self):
        db_api.register_callback(my_cb)

        con = sqlite3.connect(DB_URI, uri=True)
        cur = con.cursor()
        cur.execute("select test(?, ?)", (1, 2))
        cur.close()
        con.close()

        con = my_threading_local.a
        cur = con.cursor()
        cur.execute("select test(?, ?)", (1, 2))

    def test_create_function(self):
        self._open_a()

    def test_create_function_threading(self):
        t1 = threading.Thread(target=self._open_a)
        t2 = threading.Thread(target=self._open_a)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


if
