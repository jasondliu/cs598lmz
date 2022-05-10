import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2))

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))

def f(x):
    return x**2

f_c = FUNTYPE(f)

x = np.array([1, 2, 3], dtype=np.float64)
print(f_c(x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))))

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))

def f(x):
    return x[0]**2

f_c = FUNTYPE(f)

x = np.array
