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

lib = ctypes.CDLL("libsqlite3.so")
try:
    mydata = ctypes.pointer(ctypes.c_int())
    lib.sqlite3_open_v2("test.db", ctypes.byref(mydata), 1, None)
    conn = ctypes.cast(mydata.contents, ctypes.py_object)()
    lib.sqlite3_open_v2("test.db", ctypes.byref(mydata), 1, None)
    conn3 = ctypes.cast(mydata.contents, ctypes.py_object)()
    my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)(my_cb)
    print(conn)
    print(conn3)
    lib.sqlite3_set_authorizer(conn, my_cb_p, None)
    conn.create_function("test", 2, test_fn)
    conn3.create_function("test", 2, test_fn)
    cur = conn.c
