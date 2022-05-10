import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2))

#%%

import ctypes
import numpy as np

def f(x):
    return x**2

f_c = ctypes.CDLL('./f.so').f
f_c.restype = ctypes.c_double
f_c.argtypes = [ctypes.c_double]

x = np.linspace(0,1,100)
y = np.zeros(100)

for i in range(100):
    y[i] = f_c(x[i])

print(y)

#%%

import ctypes
import numpy as np

def f(x):
    return x**2

f_c = ctypes.CDLL('./f.so').f
f_c.restype = ctypes.c_double
f_c.argtypes = [ctypes.c_
