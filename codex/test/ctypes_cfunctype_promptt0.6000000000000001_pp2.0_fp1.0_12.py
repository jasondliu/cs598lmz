import ctypes
# Test ctypes.CFUNCTYPE()'s argtypes and restype attributes.
from ctypes import *

class X(object):
    pass

def func(i, f, c, s, u, p, z, q, r, h, v, w, t, x):
    print(i, f, c, s, u, p, z, q, r, h, v, w, t, x)

# functions with no arguments
cfunc = CFUNCTYPE(c_int)()
cfunc()

cfunc = CFUNCTYPE(c_int)
cfunc()

cfunc = CFUNCTYPE(c_int)(func)
cfunc()

cfunc = CFUNCTYPE(c_int, argtypes=())
cfunc()

cfunc = CFUNCTYPE(c_int, argtypes=[])
cfunc()

cfunc = CFUNCTYPE(c_int, argtypes=())(func)
cfunc()

cfunc = CFUNCTYPE(c_int, argtypes=[], restype=None)
c
