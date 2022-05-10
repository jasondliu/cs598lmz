import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

f_c(2.2)

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

x = np.linspace(0, 10, 100)
y = np.zeros_like(x)

for i in range(x.size):
    y[i] = f_c(x[i])

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

x = np.linspace(0, 10, 100)
y = np.
