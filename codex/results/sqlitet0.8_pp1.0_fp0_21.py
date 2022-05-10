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

dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
dll.sqlite3_shutdown.argtypes = ()
dll.sqlite3_shutdown.restype = ctypes.c_int

def fn(p):
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    cur = conn.cursor()
    cur.execute(b"select test(2, 3)")
    cur.close()
    del conn
    dll.sqlite3_shutdown()

thread = threading.Thread(target=fn, args=(my_cb,))
thread.start()
thread.join()

print(my_threading_local.a)
