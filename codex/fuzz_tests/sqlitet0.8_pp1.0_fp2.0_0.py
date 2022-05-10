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

class CTypesThread:
    def __init__(self, func, args):
        self._async_raise(func, args)

    def _async_raise(self, func, args):
        tid = _ctypes.pythonapi.PyThreadState_GetDict()
        if not tid:
            raise AssertionError("Could not get thread state dictionary")

        nid = _ctypes.pythonapi.PyLong_AsLong(_ctypes.pythonapi.PyLong_FromVoidPtr(id(self)))
        _ctypes.pythonapi.PyDict_SetItem(tid, _ctypes.py_object(nid), _ctypes.py_object(func(*args)))
        _ctypes.pythonapi.Py_DecRef(tid)

def run_in_thread(func):
    ct = CTypesThread(func, ())
    ct.join()

def test_threads():
    # Test Python threads
    run_in_thread(run_test)

    # Test native threads
    _ctypes = ctypes.cd
