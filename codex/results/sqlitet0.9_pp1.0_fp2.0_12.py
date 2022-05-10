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

try:
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    func_type = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    func = func_type(my_cb)
    p = libc.Py_NewInterpreter()
    try:
        libc.PyEval_EvalCode(func(None), None, None)
    finally:
        del my_threading_local.a
        libc.Py_EndInterpreter(p)
        libc.Py_Finalize()
finally:
    # test if the connection was correctly cleaned up in the subinterpreter
    a = sqlite3.connect(DB_URI, uri=True)
    a.close()
</code>
This test crashes python with segmentation fault if the code is changed to use the default connection factory (by just removing the factory argument to connect). 
I don't want to use the deleting_conn class so I guess I need to patch sqlite3 to support using the default connection class
