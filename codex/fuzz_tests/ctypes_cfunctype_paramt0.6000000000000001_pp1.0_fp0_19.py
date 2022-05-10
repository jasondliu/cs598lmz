import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

from pygsl import rng
from pygsl.rng import rng_types
rng_types.rng_set(rng.rng())

import pygsl.sf

def func(x):
    return x**2

func_wrap = FUNTYPE(func)
print func_wrap(3)

print pygsl.sf.erf(1)
print pygsl.sf.erf(ctypes.c_double(1))

print pygsl.sf.erf_e(1)
print pygsl.sf.erf_e(ctypes.c_double(1))

print pygsl.sf.erf_Z_e(1)
print pygsl.sf.erf_Z_e(ctypes.c_double(1))

print pygsl.sf.erf_Z(1)
print pygsl.sf.erf_Z(ctypes.c_double(1))

print pygsl.sf.er
