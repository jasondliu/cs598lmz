import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def cfunc(f, argtype=ctypes.c_double, restype=ctypes.c_double):
    return FUNTYPE((argtype,), restype)(f)

def wrapper(f, argtype=ctypes.c_double, restype=ctypes.c_double):
    def _(x):
        return f(argtype(x))
    return cfunc(_, argtype, restype)

print(math.sin(1.0))
print(wrapper(math.sin)(1.0))

def x_cb(x):
    return x * (1 - x)

cb = wrapper(x_cb, argtype=ctypes.c_float, restype=ctypes.c_float)

print(cb(0.5))

from numba import cfunc, carray
from ctypes import c_float

fn = cfunc("float (float)")(x_cb)
print(fn(0.5))

a = carray(range(10), d
