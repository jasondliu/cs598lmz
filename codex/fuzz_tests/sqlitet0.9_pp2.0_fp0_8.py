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

libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
db_open_hook = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(my_cb)
conn = sqlite3.connect(DB_URI, uri=True)
libc.sqlite3_db_config(conn.connection._handle, 4, db_open_hook)
cur = my_threading_local.a.cursor()
cur.execute("select test(?, ?)", list(range(2048)))
