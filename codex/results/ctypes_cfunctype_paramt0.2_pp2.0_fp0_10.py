import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

cfunc = FUNTYPE(f)

print(cfunc(2))

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

cfunc = FUNTYPE(f)

x = np.linspace(0, 10, 100)
y = np.zeros(x.shape)

for i in range(len(x)):
    y[i] = cfunc(x[i])

print(y)

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

cfunc = FUNTYPE(f)

x = np.linspace(0, 10, 100)
y =
