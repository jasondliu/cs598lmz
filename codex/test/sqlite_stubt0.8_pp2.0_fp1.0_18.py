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

lib = None

def setup_module():
    global lib

    lib = ctypes.CDLL(ctypes.util.find_library('c'))
    lib.set_callback(my_cb)
    lib.run_callback()

def test_sqlite3_connection():
    a = my_threading_local.a

    try:
        a.execute("select test(5, 6)").fetchone()[0]
    except sqlite3.Error:
        pass

def teardown_module():
    lib.free_callback()
