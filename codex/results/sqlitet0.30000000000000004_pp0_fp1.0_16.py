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
    my_threading_local.a.close()
    return 1

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p()))
    lib.sqlite3_create_function(ctypes.c_void_p(), "test", 1, 1, ctypes.c_void_p(), my_cb, my_cb2)
    lib.sqlite3_close(ctypes.c_void_p())

if __name__ == "__main__":
    main()
</code>
It seems that the problem is that the <code>sqlite3.Connection</code> object is being garbage collected before the <code>my_cb2</code> function is called. I've tried using <code>weakref.ref</code> to keep a reference to the connection object, but that doesn't seem to work either.
I'm using Python 3.4.2 on Windows
