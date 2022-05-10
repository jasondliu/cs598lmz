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

if __name__ == '__main__':
    class Test(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int)]

    ctypes.pythonapi.Py_InitModule4.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.py_object]
    ctypes.pythonapi.Py_InitModule4.restype = ctypes.py_object
    ctypes.pythonapi.PyModule_GetDict.argtypes = [ctypes.py_object]
    ctypes.pythonapi.PyModule_GetDict.restype = ctypes.py_object
    ctypes.pythonapi.PyDict_SetItemString.argtypes = [ctypes.py_object, ctypes.c_char_p, ctypes.py_object]

    mod = ctypes.pythonapi.Py_InitModule4(b"my_module", None, b"", None)
    dict = ctypes.pythonapi.PyModule_GetDict(mod
