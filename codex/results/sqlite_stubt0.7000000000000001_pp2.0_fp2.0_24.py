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

sqlite3.sqlite3_open_v2 = sqlite3.sqlite3_open
sqlite3.sqlite3_open = my_cb

class TestSqlite3(unittest.TestCase):
    def test_connect(self):
        c = sqlite3.connect(DB_URI, uri=True)
        c.execute("CREATE TABLE a (b)")
        c.commit()

    def test_connect_1(self):
        c = sqlite3.connect(DB_URI, uri=True)
        c.execute("CREATE TABLE a (b)")
        c.commit()

    def test_connect_2(self):
        c = sqlite3.connect(DB_URI, uri=True)
        c.execute("CREATE TABLE a (b)")
        c.commit()

    def test_connect_3(self):
        c = sqlite3.connect(DB_URI, uri=True)
        c.execute("CREATE TABLE a (b)")
        c.commit()

    def
