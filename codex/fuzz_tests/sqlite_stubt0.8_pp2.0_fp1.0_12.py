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

so_file = ctypes.util.find_library("sqlite3")
if not so_file:
    raise Exception("sqlite3 not found")

sqlite_lib = ctypes.CDLL(so_file)
sqlite_lib.sqlite3_open_v2.argtypes = [ ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p ]
sqlite_lib.sqlite3_open_v2.restype = ctypes.c_int

db_conn = ctypes.c_void_p()

sqlite_lib.sqlite3_open_v2(b"file:test?mode=memory", ctypes.byref(db_conn), 1 | 8, None)

sqlite_lib.sqlite3_set_authorizer(db_conn, my_cb, None)

sqlite_lib.sqlite3_exec(db_conn, b"SELECT test(1, 2)", None, None, None)

ct
