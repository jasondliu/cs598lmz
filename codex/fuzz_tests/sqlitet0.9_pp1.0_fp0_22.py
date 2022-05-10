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

myqlite3= ctypes.CDLL(ctypes.util.find_library('sqlite3'))
myqlite3.sqlite3_shutdown.restype = ctypes.c_int
myqlite3.sqlite3_shutdown.argtypes = ()

class MyException(Exception):
    pass

class Test(unittest.TestCase):
    def test_1(self):
        c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        c.close()

    def test_2(self):
        myqlite3.sqlite3_shutdown()
        try:
            c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        except Exception as e:
            self.assertEqual(str(e), 'library routine called out of sequence')
            raise MyException from e
        else:
            self.fail()

    def test_3(self):
        c = sqlite3.connect(DB_URI, uri=
