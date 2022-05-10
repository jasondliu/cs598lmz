import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_as_cfunc = FUNTYPE(f)

print(f_as_cfunc(2.0))

#%%

#%%

import numpy as np

def f(x):
    return x**2

f_as_cfunc = FUNTYPE(f)

x = np.linspace(0, 1, 10)

y = np.zeros_like(x)

for i in range(len(x)):
    y[i] = f_as_cfunc(x[i])

print(y)

#%%

import numpy as np

def f(x):
    return x**2

f_as_cfunc = FUNTYPE(f)

x = np.linspace(0, 1, 10)

y = np.zeros_like(x)

for i in range(len(x)):
    y[i] = f_as_cfunc(x
