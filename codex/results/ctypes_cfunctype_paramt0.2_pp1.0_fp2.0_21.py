import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)

f(2)

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)

f(2)

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)

f(2)

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)

f(2)
