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

sqlite3.enable_callback_tracebacks(True)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_exec.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
]

db = sqlite3.connect(DB_URI, uri=True)

db.executemany("select test(?, ?)", ((1, 2),))

lib.sqlite3_exec(db.connection, b"select test(1, 2)", None, None, None)

lib.sqlite3_exec(
    db.connection,
    b"select test(1, 2)",
    ctypes.c_void_p(my_cb),
    None,
    None,
)

db.executemany("select test(?, ?)", ((1, 2),))

lib.sql
