import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback

# the callback is called with a pointer to a structure
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

Xp = ctypes.POINTER(X)

@ctypes.CFUNCTYPE(ctypes.c_int, Xp)
def callback(x):
    print(x.contents.a, x.contents.b)
    return x.contents.a + x.contents.b

lib.pass_x(callback)

# the callback is called with a pointer to a structure
# and a pointer to a function
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

Yp = ctypes.POINTER(Y)

@ctypes.CFUNCT
