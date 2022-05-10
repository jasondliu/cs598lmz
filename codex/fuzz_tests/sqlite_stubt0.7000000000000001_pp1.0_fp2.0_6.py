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

class test_sqlite3_threading(unittest.TestCase):
    def test_threading(self):
        ctypes.pythonapi.Py_AddPendingCall(my_cb, None)

        while not hasattr(my_threading_local, "a"):
            time.sleep(0.1)

        self.assertEqual(my_threading_local.a.execute("select test(5,10)").fetchone()[0], 5)

class test_sqlite3(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        self.cur = self.con.cursor()
        self.cur.execute('create table test(c1, c2)')

    def tearDown(self):
        self.con.close()

    def CheckPragmaTableInfo(self, table, expected):
        sql = 'pragma table_info(%s)' % table
        cursor = self.con
