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

def test_my_cb():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    lib.sqlite3_test_introspect(callback, None)

test_my_cb()
</code>
The above code is the minimum I can write to reproduce the error:
<code># python3.3 test.py
# Fatal Python error: PyEval_SaveThread: NULL tstate

#python2.7 test.py
# Fatal Python error: PyEval_SaveThread: NULL tstate

#python2.6 test.py
# Fatal Python error: PyThreadState_Get: NULL tstate
</code>

