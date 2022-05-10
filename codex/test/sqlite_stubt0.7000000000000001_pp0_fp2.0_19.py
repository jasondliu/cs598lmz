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

def my_cb2(p):
    my_threading_local.a.close()
    return 1

class MyTestCase(unittest.TestCase):
    def test_concurrent_access(self):
        dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        dll.sqlite3_config(ctypes.c_int(3), ctypes.c_int(1))
        dll.sqlite3_config(ctypes.c_int(4), ctypes.py_object(my_cb))
        dll.sqlite3_config(ctypes.c_int(7), ctypes.py_object(my_cb2))
        db = sqlite3.connect(DB_URI, uri=True)

        def tfn(db):
            db.execute("select test(3, 5);")

        threading.Thread(target=tfn, args=(db,)).start()
        threading.Thread(target=tfn, args=(db,)).start()

