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

ctypes.pythonapi.Py_InitModule4.argtypes = [ctypes.c_char_p, ctypes.py_object, ctypes.c_char_p, ctypes.py_object, ctypes.c_int]
ctypes.pythonapi.Py_InitModule4.restype = ctypes.py_object
ctypes.pythonapi.Py_InitModule4(ctypes.c_char_p("pytest6588"), ctypes.py_object({"test_fn" : ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(my_cb)}), ctypes.c_char_p(""), ctypes.py_object(None), 1)

my_cb(1)

# try to get rid of the now stale Connection to provoke bug 6588
del my_threading_local.a

# do something with the deleted connection to provoke the error
my_threading_local.a.execute("select test(?, ?)", (1, 2))
