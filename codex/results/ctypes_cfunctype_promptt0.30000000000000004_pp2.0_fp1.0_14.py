import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

lib.my_callback.argtypes = [ctypes.c_int, ctypes.POINTER(X), ctypes.POINTER(Y), ctypes.POINTER(Z)]
lib.my_callback.restype = ctypes.c_int

def callback(a, x, y, z):
    print(a, x.contents.a, x.contents.b, y.contents.a, y.contents.b, z.
