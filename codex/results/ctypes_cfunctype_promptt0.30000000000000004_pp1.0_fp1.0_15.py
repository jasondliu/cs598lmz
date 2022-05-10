import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a pointer argument
# and a pointer return value

prototype = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

paramflags = (1, "paramflags"),

def func(*args):
    return prototype(("func", lib), paramflags)(*args)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X()
x.a = 42

addr = func(ctypes.byref(x))
assert addr == ctypes.addressof(x)

# call a function with a pointer argument
# and a simple return value

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

def func(*args):
    return prototype(("func_int", lib), paramflags)(*args)

addr = func(ct
