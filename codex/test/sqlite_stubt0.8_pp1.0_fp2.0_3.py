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

def my_cb2(p):
    a = my_threading_local.a
    print ("Connection:", a)
    res = a.execute("select test(?, 3)", [5]).fetchone()
    print (res)
    return 1

def my_cb3(p):
    print ("Deleting connection")
    a = my_threading_local.a
    del a

def my_cb4(p):
    print ("Last callback")
    libtest.test_finalize(None)

libtest = ctypes.CDLL(ctypes.util.find_library("test"))
libtest.test_init(None)
libtest.register_callback(my_cb, my_cb2, my_cb3, my_cb4)
libtest.test_run_threads()
