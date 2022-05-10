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

def test_func(a, b):
    return a

def test_func_with_error(a, b):
    raise ValueError("test error")

class SQLiteFunctionTests(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.create_function("test", 2, test_func)
        self.con.create_function("test_with_error", 2, test_func_with_error)
        self.cur = self.con.cursor()

    def CheckCallFunc(self, function, in_args, expected):
        in_args = tuple([sqlite3.prepare_for_test(x) for x in in_args])
        self.assertEqual(self.cur.execute("select " + function + "(?, ?)",
                                          in_args).fetchone()[0], expected)

    def test_basic_call(self):
        self.CheckCallFunc("test", (1, 2), 1)

    def test
