import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2))

#%%

import ctypes

def f(x):
    return x**2

f_c = ctypes.CDLL('./libf.so').f
f_c.restype = ctypes.c_double
f_c.argtypes = [ctypes.c_double]

print(f_c(2))

#%%

import ctypes

def f(x):
    return x**2

f_c = ctypes.CDLL('./libf.so').f
f_c.restype = ctypes.c_double
f_c.argtypes = [ctypes.c_double]

print(f_c(2))

#%%

import ctypes

def f(x):
    return x**2

f_c = ctypes.CDLL('./libf.so').f

