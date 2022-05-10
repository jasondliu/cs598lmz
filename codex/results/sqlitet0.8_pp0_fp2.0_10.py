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

def test_callback():
    a = sqlite3.connect(':memory:', uri=True)
    ctypes.pythonapi.Py_InitModule4.restype=ctypes.py_object
    ctypes.pythonapi.Py_InitModule4.argtypes=(ctypes.c_char_p,ctypes.POINTER(ctypes.py_object),ctypes.c_char_p,ctypes.py_object,ctypes.c_int)
    
    m = ctypes.pythonapi.Py_InitModule4('pysqlite_test', None,
                                        'This is a pysqlite test module',
                                        None, 1)

    d = {'step':my_cb, 'finalize':my_cb}

    for k, v in d.items():
        a.create_function(k, 1, v)

    a.execute('SELECT step()')

    assert my_threading_local.a

    def test_fn(a, b):
        return my_threading_local.a

    my_threading_local
