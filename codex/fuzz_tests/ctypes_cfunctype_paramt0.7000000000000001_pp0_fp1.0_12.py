import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return math.sin(x)

f_cfunctype = FUNTYPE(f)

import numpy as np

# Example 1: a Python function
print('f(0.5) = %f' % f(0.5))

# Example 2: a NumPy ufunc
print('sin(0.5) = %f' % np.sin(0.5))

# Example 3: a C function through ctypes
print('f_cfunc(0.5) = %f' % f_cfunctype(0.5))

# Example 4: a C function with Numba
f_numba = numba.jit(f_cfunctype)
print('f_numba(0.5) = %f' % f_numba(0.5))

# Example 5: a C function through Cython
%load_ext Cython
 
# Import the function from the Cython module
from cython_example_1 import f
