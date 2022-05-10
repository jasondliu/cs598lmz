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

    return 1.0

def my_load_callback(p):
    return 1.0

def my_abort_callback(p, err_number, err_message):
    return 1

def my_commit_callback(p):
    return 0

def my_update_callback(p, sql_type, database_name, table_name, row_id):
    return 0

def my_rollback_callback(p):
    return 0

def my_busy_callback(p, retries):
    return 1

class TestCase(unittest.TestCase):
    def setUp(self):
        clib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.db = clib.sqlite3_malloc(ctypes.sizeof(ctypes.c_void_p))
        self.clib = clib
        self.callback_called = 0
        self.callback_called_lock = threading.Lock()

        self.conn = sqlite3.connect(DB_URI, uri=True)


