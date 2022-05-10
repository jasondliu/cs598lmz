import ctypes
# Test ctypes.CFUNCTYPE.
import _ctypes_test
lib = _ctypes_test.dll

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_float)]

Xp = ctypes.POINTER(X)
Yp = ctypes.POINTER(Y)

class Z(ctypes.Union):
    _fields_ = [("x", Xp),
                ("y", Yp)]

Zp = ctypes.POINTER(Z)

f = lib.sum_floats
f.restype = ctypes.c_float
f.argtypes = (Zp, ctypes.c_int)

def callback(x, y):
    return x.contents.a + y

def callback_ffi(x, y):
    return x.a + y

s = Z()
s.x = X(21)

CMPFUNC = ctypes.CFUNCTYPE(ctypes
