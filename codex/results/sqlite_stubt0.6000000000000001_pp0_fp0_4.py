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

def test():
    ctypes.pythonapi.Py_AddPendingCall(ctypes.pythonapi.PyThreadState_Get,
        my_cb)
    ctypes.pythonapi.Py_AddPendingCall(ctypes.pythonapi.PyThreadState_Get,
        my_cb2)

test()
</code>
The error message is
<code>Exception exceptions.AttributeError: "'deleting_conn' object has no attribute 'close'" in &lt;bound method deleting_conn.__del__ of &lt;__main__.deleting_conn object at 0xb75b9f2c&gt;&gt; ignored
</code>
which is weird because if I remove the create_function call, it works fine.

