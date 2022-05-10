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

# test that the function works with threads
def thread_test():
    my_cb(None)
    assert my_threading_local.a


# test that the registered function is called and
# the context freed (this test will crash if it fails)
def test():
    fn = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    z = ctypes.c_void_p(0)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open("test", ctypes.byref(z))
    lib.sqlite3_create_function(z, "test", 2, 1, 0, fn, 0, 0)
    lib.sqlite3_close(z)

if __name__ == '__main__':
    test()
    thread_test()
    print("success!")
