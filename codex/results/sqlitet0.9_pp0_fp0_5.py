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

extension_module = ctypes.util.find_library("mytest.so")
# extension_module = "mytest.so"

my_test = ctypes.CDLL(extension_module, use_errno=True)

if not hasattr(my_test, "sqlite3_extension_init"):
    raise Exception("Couldn't find sqlite3_extension_init in extension")

my_test.sqlite3_extension_init.argtypes = [ctypes.c_int]

MY_SQLITE_EXTENSION_INIT1 = 179

ret = my_test.sqlite3_extension_init(MY_SQLITE_EXTENSION_INIT1, ctypes.cast(ctypes.pythonapi.PyCapsule_New(my_cb, None, None), ctypes.c_void_p))
</code>
And here are my C++ files:
<code>// my_test.cpp
#include &lt;Python.h&gt;
#include &lt;sqlite3ext.h&gt
