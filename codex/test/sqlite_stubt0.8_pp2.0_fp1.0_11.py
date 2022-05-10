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

def my_cb_final(p):
    b = my_threading_local.a
    return 1

class Test(unittest.TestCase):
    def test_cb_fn(self):
        lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
        lib.sqlite3_reset_auto_extension()


        lib.sqlite3_auto_extension(my_cb)

        db = sqlite3.connect(DB_URI, uri=True)

        db.create_function("test", 2, lambda a, b: a)

        cur = db.cursor()
        try:
            cur.execute("select test(0, 0)")
            self.assertEqual(cur.fetchone()[0], 0)
        finally:
            cur.close()

        cur = db.cursor()
