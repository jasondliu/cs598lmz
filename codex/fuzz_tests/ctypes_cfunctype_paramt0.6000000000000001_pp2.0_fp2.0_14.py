import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def force_py(r):
    return lj(r, 1.0, 1.0)

force_c = FUNTYPE(force_py)

def force_d(r):
    return force_c(r)

print(force_d(2.0))

from numba import jit
force_numba = jit(force_py)

def force_n(r):
    return force_numba(r)

print(force_n(2.0))

from numba.pycc import CC
cc = CC('lj_force')
cc.export('lj', 'f8(f8, f8, f8)')(lj)
cc.compile()

from lj_force import lj as force_cc

def force_cc_caller(r):
    return force_cc(r, 1.0, 1.0)

print(force_cc_caller(2.0))

from pyopencl import clmath

