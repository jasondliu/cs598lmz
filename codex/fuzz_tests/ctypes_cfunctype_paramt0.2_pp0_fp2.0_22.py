import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

func_c = FUNTYPE(func)

print(func_c(2))

#%%

import ctypes
import numpy as np

def func(x):
    return x**2

func_c = np.vectorize(func)

print(func_c(2))

#%%

import ctypes
import numpy as np

def func(x):
    return x**2

func_c = np.vectorize(func)

print(func_c(2))

#%%

import ctypes
import numpy as np

def func(x):
    return x**2

func_c = np.vectorize(func)

print(func_c(2))

#%%

import ctypes
import numpy as np

def func(x):
    return x**2

func_c = np.vectorize(func)

print(func_c(2))

#
