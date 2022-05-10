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

dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
dll.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]

conn_p = ctypes.c_void_p()
dll.sqlite3_open(DB_URI.encode(), ctypes.byref(conn_p))

dll.sqlite3_create_function(conn_p, b"test", 1, ctypes.c_int(0), ctypes.c_void_p(), my_cb, None, None)
dll.sqlite3_close(conn_p)

thread = threading.Thread(target=my_cb, args=(0,))
thread.start()
thread.join()

con = sqlite3.connect(DB_URI, uri=True)
cur = con.cursor()

cur.execute("SELECT test(1, 2)")
print(cur.fetchone())

con.close()
