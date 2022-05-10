import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x*x

fptr = FUNTYPE(func)
fptr(2)

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x*x

fptr = FUNTYPE(func)
fptr(2)

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x*x

fptr = FUNTYPE(func)
fptr(2)

#%%

import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x*x

fptr = FUNTYPE(func)
f
