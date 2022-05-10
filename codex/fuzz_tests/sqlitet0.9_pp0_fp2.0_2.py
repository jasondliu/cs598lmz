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

p = types.PythonObject(my_cb)

m = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.POINTER(ctypes.py_object)
)(p)

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
lib.c_func(m)
</code>
It crashed with:
<code>Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)
</code>
I noticed the <code>libsqlite.so</code> was also loaded when I was debugging it with gdb, and I don't know whether it's the reason that caused my crash. I wonder if there is any other way to create a custom sqlite connection object in the ctypes callback function.

