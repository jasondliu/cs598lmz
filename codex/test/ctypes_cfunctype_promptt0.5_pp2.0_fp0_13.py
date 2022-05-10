import ctypes
# Test ctypes.CFUNCTYPE() with a function that returns a pointer.
import _ctypes_test

prototype = ctypes.CFUNCTYPE(ctypes.c_void_p)

class X(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(ctypes.c_int))]

@prototype
def func():
    return X(p=ctypes.pointer(ctypes.c_int(42))).p

p = func()
