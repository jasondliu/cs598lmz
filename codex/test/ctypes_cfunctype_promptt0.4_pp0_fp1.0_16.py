import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_double)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

def callback(x, y):
    return x.a * y

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, X, ctypes.c_int)

# This is the function to test.  ffi.callback() takes a Python
# function and returns a foreign function that calls back to Python.
# The foreign function has the same signature as the Python function.
