import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test a simple function call
#

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
paramflags = (1, "x")

def func(*args):
    return args[0] * 2

CMPFUNC = prototype(func, paramflags)

res = lib.call_function(CMPFUNC, 3)
if res != 6:
    raise RuntimeError("%d != 6" % res)

#
# Test a function call with a structure as parameter
#

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

prototype = ctypes.CFUNCTYPE(ctypes.c_int, X)
paramflags = (1, "x")

def func(*args):
    return args[0].a * args[0].b

C
