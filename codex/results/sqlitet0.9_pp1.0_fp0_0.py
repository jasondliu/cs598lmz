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

cb_ptr = ctypes.cast(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb), ctypes.c_void_p)

dll = ctypes.CDLL(ctypes.util.find_library("c"))
dll.ffi_prep_closure.restype = ctypes.c_void_p
dll.ffi_prep_closure.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

class SqliteTests(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def tearDown(self):
        self.con.close()
        self.con = None
        self.destroy_table()

    def destroy_table(self):
        # If a test has started a transaction and failed, abort it.
        try:
            self.con.execute('ROLL
