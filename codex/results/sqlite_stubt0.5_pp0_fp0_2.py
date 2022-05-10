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

def create_c_callback():
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    return ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
my_callback = create_c_callback()

libsqlite3.sqlite3_exec.argtypes = [ctypes.c_void_p, ctypes.c_char_p, callback_type, ctypes.c_void_p, ctypes.c_void_p]
libsqlite3.sqlite3_exec.restype = ctypes.c_int

db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
db.execute("create table test(a)")

res = libsqlite3.sqlite3_
