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

class SQLiteExtension(object):
    def __init__(self, path):
        self.lib = ctypes.CDLL(path)
        self.lib.sqlite3_extension_init.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p]
        self.lib.sqlite3_extension_init.restype = None

    def load(self, db):
        self.lib.sqlite3_extension_init(db.sqlite_handle, None, None)

def test_threads():
    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    db.enable_load_extension(True)
    db.create_function("my_cb", 1, my_cb)

    extension = SQLiteExtension(ctypes.util.find_library("sqlite3_test_extension"))
    extension.load(db)

    db.execute("SELECT my_cb(1)")

    t1 = threading
