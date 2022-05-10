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

class SQLiteThreadingTests(unittest.TestCase):

    def setUp(self):
        # 0. Enable extended result codes
        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        lib.sqlite3_enable_load_extension(None, 1)

        # 1. Register the callback
        self.assertEqual(
            0,
            lib.sqlite3_autoconnect(my_cb)
        )

        # 2. Get the connection
        self.conn = sqlite3.connect(DB_URI, uri=True)
        self.conn.row_factory = sqlite3.Row

    def tearDown(self):
        # Clear out the threading local
        del my_threading_local.__dict__['a']

    def test_simple(self):
        cur = self.conn.cursor()

        cur.execute("select test(1, 2);")
        self.assertEqual(1, cur.fetchone()[0])

        cur.execute("select test(
