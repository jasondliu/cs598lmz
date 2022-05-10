import ctypes
# Test ctypes.CFUNCTYPE for non-void return types
import _ctypes_test

lib = _ctypes_test.dll

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

def func(a):
    return X(a)

CMPFUNC = ctypes.CFUNCTYPE(X, ctypes.c_int)

cfunc = CMPFUNC(func)
p = lib.set_cmp_func(cfunc)
print lib.get_cmp_func()(2)
lib.set_cmp_func(p)
print lib.get_cmp_func()(2)
