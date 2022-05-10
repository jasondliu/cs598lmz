import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is called with a function pointer as first argument.
# The function pointer is called with a pointer to a structure as
# first argument.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(X))

def callback(x):
    print(x.contents.a, x.contents.b)
    return x.contents.a + x.contents.b

CALLBACKFUNC = CALLBACK(callback)

lib.pass_func(CALLBACKFUNC)

# This function is called with a function pointer as first argument.
# The function pointer is called with a pointer to a structure as
# first argument.

class Y(ctypes.Structure):
    _fields_ = [("a", c
