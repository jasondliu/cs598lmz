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

try:
    libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
except Exception:
    libsqlite3 = None

if libsqlite3:
    x = ctypes.c_int()
    y = ctypes.c_void_p()
    libsqlite3.sqlite3_config(2, my_cb, ctypes.byref(y))


class test_callback(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.con = sqlite3.connect(DB_URI, uri=True)
        cur = cls.con.cursor()
        cur.execute('CREATE TABLE test(id)')

    @classmethod
    def tearDownClass(cls):
        cls.con.close()

    def test_callback(self):
        self.con.execute('CREATE TABLE test(id)')

class test_enable_load_extension(unittest.TestCase):
    def setUp
