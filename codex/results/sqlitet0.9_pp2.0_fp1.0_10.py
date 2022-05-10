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

    return 100.0 * (p / 100.0)

libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_progress_handler.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
libsqlite3.sqlite3_progress_handler.restype = None
libsqlite3.sqlite3_progress_handler.errcheck = lambda result, func, args: None

progress_cb = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)(my_cb)

with closing(sqlite3.connect(":memory:", uri=True, factory=deleting_conn)) as conn:
    conn.execute("create table test (a INT);")
    conn.execute("insert into test values (1);")
    cursor = conn.cursor()
    libsqlite3.sqlite3_progress_handler(cursor.connection.
