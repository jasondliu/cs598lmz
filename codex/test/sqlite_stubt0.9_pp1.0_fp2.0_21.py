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

try:
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
except OSError:
    raise Exception("can't find sqlite3 library")

lib.sqlite3_config(0)

def callback(user_p, msg):
    if user_p:
        pass

conn_ptr = lib.sqlite3_initialize()
assert conn_ptr, "failed to initialize sqlite3"

if not lib.sqlite3_config(4, callback, None):
    pass

lib.sqlite3_create_function(conn_ptr, b"my_cb", 0, 1, 0, my_cb, 0)

db_uri = DB_URI.encode('ascii')
retcode = lib.sqlite3_open_v2(db_uri, ctypes.byref(ctypes.pointer(conn_ptr)), 1, None)

assert retcode == 0

con = sqlite3.dbapi2.Connection(DB_URI)

