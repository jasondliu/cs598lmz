import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

libc = ctypes.CDLL(ctypes.util.find_library("c"))

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

def func(p1, p2):
    print "func() called"
    return p1.a + p2.b

py_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(X), ctypes.POINTER(Y))(func)
print "py_func is", py_func

print "calling the C function"
p1 = X(3)
p2 = Y(4)
res = libc.call_func(py_func, ctypes.byref(p1), ctypes.byref(p2))
print "call_func() returned", res
