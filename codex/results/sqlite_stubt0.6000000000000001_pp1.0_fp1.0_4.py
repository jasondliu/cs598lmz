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

    return 100

def my_cb2(p):
    print "my_cb2"
    a = my_threading_local.a
    a.execute("select test(1, 2)")
    return 0

if __name__ == '__main__':
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_config(ctypes.c_int(2), ctypes.c_int(0))

    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    lib.sqlite3_config(ctypes.c_int(4), cb)

    cb2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb2)
    lib.sqlite3_config(ctypes.c_int(4), cb2)

    print "starting"
    a = sqlite3.connect(DB_URI, uri=True
