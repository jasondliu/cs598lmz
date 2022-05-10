import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = _ctypes_test.dll

# XXX This is a bit too complicated, but it is the only way to
# XXX get the function address to pass it to the CFUNCTYPE
# XXX constructor.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int)]

Xp = ctypes.POINTER(X)
Yp = ctypes.POINTER(Y)
Zp = ctypes.POINTER(Z)

f1 = lib.my_callback1
f1.argtypes = [Xp, Yp, Zp]
f1.restype = ctypes.c_int

f2 = lib.my_callback2
f2.argtypes = [Xp, Yp, Zp]
f2.restype
