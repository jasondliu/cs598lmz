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
libc.atexit(my_cb)
</code>
When I run this, I get the following error:
<code>ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: Don't know how to convert parameter 1
</code>
I've tried various types of function pointer and callback types, but I always get a type error.


A:

What you are trying to do is not possible. Python's <code>ctypes</code> module can only pass pointers to C functions. C functions are compiled as <code>static</code> functions and therefore can only be called directly. There is no way to call a Python callable from a C function, because the Python runtime is not initialized at that point.
The best you can do is to initialize the Python runtime from a C function, which is the task of the <code>Py_Initialize()</code> function. This function can be called repeatedly, but you need to keep track of whether it has been called before, so you don't try to initialize twice
