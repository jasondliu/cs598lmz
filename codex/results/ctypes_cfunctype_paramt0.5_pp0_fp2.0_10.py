import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def add(x, y):
    return x + y

add_c = FUNTYPE(add)

print(add_c(1, 2))

#%%
import ctypes
from ctypes import c_int

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, c_int, c_int)

def add(x, y):
    return x + y

add_c = FUNTYPE(add)

print(add_c(1, 2))

#%%
import ctypes
from ctypes import c_int

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, c_int, c_int)

def add(x, y):
    return x + y

add_c = FUNTYPE(add)

print(add_c(1, 2))

#%%
import ctypes
from ctypes import c_int

FUNTYPE = ctypes.CFUNCTYPE(
