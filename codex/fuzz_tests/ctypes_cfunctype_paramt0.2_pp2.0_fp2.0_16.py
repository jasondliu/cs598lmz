import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2))

#%%
import numpy as np
import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int)

def f(x, n):
    return np.sum(x)

f_c = FUNTYPE(f)

x = np.arange(10, dtype=np.float64)

print(f_c(x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), x.size))

#%%
import numpy as np
import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int)

def f(x, n):
    return np.sum
