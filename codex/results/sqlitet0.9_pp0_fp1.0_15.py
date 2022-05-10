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

class MyTestCase(unittest.TestCase):
    def test(self):
        mydll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        mydll.sqlite3_enable_shared_cache(1)

        p = mydll.sqlite3_config(mydll.SQLITE_CONFIG_URI, 1)
        self.assertEquals(0, p)
        p = mydll.sqlite3_config(mydll.SQLITE_CONFIG_LOG, test_fn)

        # create a database and run some queries
        conn1 = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

        def test_fn(a):
            return a

        conn1.create_function("test", 1, test_fn)
        cur1 = conn1.cursor()
        cur1.execute("create table test (x, y)")
        cur1.execute("insert into test values (?, ?)", (1, 2))

        conn2 = sqlite3.connect(DB_
