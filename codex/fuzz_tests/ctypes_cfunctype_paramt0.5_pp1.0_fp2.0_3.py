import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x+1

cfunc = FUNTYPE(func)

cfunc(1)

# 2.2

import ctypes
import numpy as np

# Create arrays
a = np.random.rand(1,2)
b = np.random.rand(1,2)

# Create ctypes
a_ctypes = a.ctypes
b_ctypes = b.ctypes

# Create ctypes pointer
a_ctypes_ptr = ctypes.cast(a_ctypes.data, ctypes.POINTER(ctypes.c_double))
b_ctypes_ptr = ctypes.cast(b_ctypes.data, ctypes.POINTER(ctypes.c_double))

# Define C function
cfunc = ctypes.CDLL("./libcfunc.so")
cfunc.cfunc.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes
