import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
print("Checking sqlite3 function...")
sqlite_connect = sqlite3.connect(":memory:")
sqlite_connect.close()
print("OK")

# Test _PyObject_GC_New()
print("Checking _PyObject_GC_New()...")
_PyObject_GC_New = ctypes.pythonapi._PyObject_GC_New
_PyObject_GC_New.restype = ctypes.py_object
_PyObject_GC_New.argtypes = (ctypes.py_object,)
try:
    class TestObject(ctypes.Structure):
        _fields_ = [("value", ctypes.c_int)]
    test_object = _PyObject_GC_New(TestObject)
    print("OK. created an object with value=%d" % test_object.value)
except AttributeError:
    print("FAIL. _PyObject_GC_New() call failed")

# Test ctypes.CDLL()
print("Checking ctypes.CDLL()...")
try:
    ctypes.CDLL
