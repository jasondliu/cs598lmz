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

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.atexit.restype = ctypes.c_int
libc.atexit.argtypes = [ctypes.c_void_p]
libc.atexit(ctypes.c_void_p(my_cb))

def fn():
    a = my_threading_local.a
    a.cursor().execute("select test(1, 2)")
    a.cursor().execute("select test(2, 3)")

t = threading.Thread(target=fn)
t.start()
t.join()

print("ok")
