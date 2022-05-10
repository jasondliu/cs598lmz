import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double,ctypes.c_double)
def f(x,y):
    return x*y
f_ptr = FUNTYPE(f)
f_ptr(3.0,4.0)
import numpy as np
N = 50000
arr_f = np.frompyfunc(f,2,1)
#%timeit arr_f(np.arange(N),np.arange(N))
%timeit np.frompyfunc(f,2,1)(np.arange(N),np.arange(N))
np.frompyfunc(f,2,1)(np.arange(N),np.arange(N))
arr = np.arange(N)
%timeit f_ptr(arr,arr)

#%timeit f(arr,arr)


import ctypes
from ctypes import c_int
from ctypes import c_double

# function that takes two c_int and returns a c_int
def func(x,y):
    return x*y

# function
