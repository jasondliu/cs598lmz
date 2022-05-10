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

def my_cb_close(p):
    #print("close")
    my_threading_local.a.close()
    my_threading_local.a = None

    return 1

class TestURIDelete(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        self.db.create_function("test_uri", 0, my_cb)
        self.db.set_authorizer(my_cb_close, None)
        self.cur = self.db.cursor()

    def tearDown(self):
        try:
            self.db.close()
        except Exception:
            pass

    def test_uri_delete(self):
        cur = self.db.cursor()

        cur.execute("select test_uri();")

        cur.execute("select test('a', 'b');")
        self.assertEqual(cur.fetchone()[0], 'a')

        cur.execute("
