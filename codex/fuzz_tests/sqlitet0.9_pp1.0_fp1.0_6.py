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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
#lib = ctypes.CDLL("C:\\Program Files\\SQLite3\\lib\\sqlite3.dll")

p = ctypes.c_void_p()

lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(p))

lib.sqlite3_busy_timeout(p, 1000)

lib.sqlite3_exec(p, "CREATE TABLE t1 (a, b);", None, None, None)

lib.sqlite3_exec(p, b"INSERT INTO t1 (a, b) VALUES (?, ?)", my_cb, None, None)

def p(s):
    if isinstance(s, bytes): return s
    return s.encode("utf-8")

def test_fn(a, b):
    a = my_threading_local.a
    a.execute("INSERT INTO t1 (a, b) VALUES (?, ?)", (a,
