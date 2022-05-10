import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()

import numpy as np
array_1d_int = np.ctypeslib.ndpointer(dtype=np.int, ndim=1, flags='CONTIGUOUS')

@FUNTYPE
def fun(x):
    return x + 42

fun.restype = array_1d_int
fun.argtypes = [array_1d_int]

a = np.array([1, 2, 3], dtype=np.int)
fun(a)

#this doesn't work
#fun.restype = ctypes.c_int
#fun.argtypes = [array_1d_int]
#fun(a)
