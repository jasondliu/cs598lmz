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

ctypes.pythonapi.PyEval_ReInitThreads()
p = ctypes.pythonapi.Py_NewInterpreter()
if p == 0:
    raise RuntimeError("Py_NewInterpreter failed")
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ctypes.pythonapi.Py_EndInterpreter(p))
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ctypes.pythonapi.Py_NewInterpreter().__class__)
print(ct
