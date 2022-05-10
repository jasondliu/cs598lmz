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

if __name__ == "__main__":
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    p = ctypes.POINTER(ctypes.c_int)()

    lib.sqlite3_open_v2(b"test", ctypes.byref(p), 0x0003, None)
    lib.sqlite3_exec(p, "CREATE TABLE foo(bar)", None, None, None)

    if lib.sqlite3_set_authorizer(p, my_cb, None):
        raise RuntimeError("Couldn't set authorizer")

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.set_authorizer(my_cb)

    my_threading_local.a.row_factory = sqlite3.Row
    cursor = my_threading_local.a.execute("SELECT * FROM foo")
    row = cursor.fetchone()

    print(row.keys())
    print(row[0])
   
