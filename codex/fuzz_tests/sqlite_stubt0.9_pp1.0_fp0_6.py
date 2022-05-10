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

def my_cb2(a, b):
    return 1

class TestThreading(unittest.TestCase):
    # https://groups.google.com/d/msg/python-sqlite/AjUwpZPKOSg/3qxBo1luC-EJ
    def setUp(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        self.conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def tearDown(self):
        self.assert_("SELECT test(1,2)" in self.conn.iterdump())
        self.conn.close()

    def test_shared_cursors(self):
        cur = self.conn.cursor()
        cur.execute("PRAGMA cache_size = 10")
        cur.execute("CREATE TABLE data (x int)")
        for i in range(11):
            cur.execute("INSERT INTO data VALUES (?)", (i,))
        self
