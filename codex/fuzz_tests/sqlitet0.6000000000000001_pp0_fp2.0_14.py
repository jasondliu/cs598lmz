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
    my_threading_local.a.close()
    return 1

class TestCreateFunction(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def tearDown(self):
        self.db.close()

    def test_create_function(self):
        db = self.db
        def test_fn(a, b):
            return a

        db.create_function("test", 2, test_fn)
        self.assertEqual(db.execute("select test(1, 2)").fetchone()[0], 1)

        def test_fn(a, b):
            return a

        db.create_function("test", 2, test_fn)
        self.assertEqual(db.execute("select test(1, 2)").fetchone()[0], 1)

        def test_fn(a):
            return a

        db.create_function("test",
