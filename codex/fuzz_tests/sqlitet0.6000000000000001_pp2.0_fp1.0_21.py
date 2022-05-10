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

def test_func(p, a, b):
    return a

class SQLiteThreadingTests(unittest.TestCase):

    def setUp(self):
        self.interp = sqlite3.enable_callback_tracebacks(True)

    def tearDown(self):
        self.interp = sqlite3.enable_callback_tracebacks(False)

    def CheckCallback(self, conn, create_func, test_func, args=()):
        conn.create_function("test_func", len(args), test_func)
        cur = conn.cursor()
        cur.execute("select test_func(%s)" % ','.join(["?"] * len(args)), args)
        value = cur.fetchone()[0]
        self.assertEqual(value, args[0])

    def test_threading(self):
        # This test checks that it is safe to access the same connection
        # from different threads.

        # First, check that it is safe to share a connection

        conn = sqlite3.connect(DB
