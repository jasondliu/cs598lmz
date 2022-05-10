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

def my_cb_err(p, x, y):
    if my_threading_local.a:
        my_threading_local.a.close()

sqlite3.enable_callback_tracebacks(True)

try:
    sqlite3.set_authorizer(my_cb)
    sqlite3.threadsafety
except Exception as e:
    pass

sqlite3.set_authorizer(my_cb)

conn = sqlite3.connect(DB_URI, uri=True)
cur = conn.cursor()
print(cur.execute("select test(1, 2)").fetchall())

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

lib.sqlite3_set_authorizer(conn._sqlite3_conn, my_cb, my_cb_err)
print(cur.execute("select test(1, 2)").fetchall())

cur.close()
conn.close()
