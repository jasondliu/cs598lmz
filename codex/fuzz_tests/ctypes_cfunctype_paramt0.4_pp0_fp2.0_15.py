import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def c_f(x):
    return x**2

c_f_ptr = FUNTYPE(c_f)

def f(x):
    return x**2

f_ptr = FUNTYPE(f)

print(c_f_ptr(1))
print(f_ptr(1))

#%%
# example 2
import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))

def c_f(x):
    return x[0]**2 + x[1]**2

c_f_ptr = FUNTYPE(c_f)

def f(x):
    return x[0]**2 + x[1]**2

f_ptr = FUNTYPE(f)

x = np.array([1, 2], dtype=np.float64)
print(c_f_ptr(x.ctypes.data_as(ctypes
