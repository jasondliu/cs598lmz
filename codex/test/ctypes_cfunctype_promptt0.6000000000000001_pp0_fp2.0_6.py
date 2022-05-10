import ctypes
# Test ctypes.CFUNCTYPE with a function pointer as argument.

from ctypes import *

def func(pf):
    print(pf.__class__)
    return pf(42)

PyCFuncPtrType = CFUNCTYPE(c_int, c_int)
pf = PyCFuncPtrType(lambda x: x*2)

assert func(pf) == 84

PFuncPtrType = CFUNCTYPE(c_int, POINTER(c_int))
pf = PFuncPtrType(lambda x: x[0]*2)

