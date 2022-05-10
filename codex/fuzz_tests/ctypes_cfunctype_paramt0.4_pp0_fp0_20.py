import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x,y):
    return x*y

f_c = FUNTYPE(f)
print(f_c(3,4))

#%%

#%%
import ctypes
import numpy as np

#%%

#%%
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x,y):
    return x*y

f_c = FUNTYPE(f)
print(f_c(3,4))

#%%

#%%
import ctypes
import numpy as np

#%%

#%%
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x,y):
    return x*y

f_c = FUNTYPE(f)
print(f_c(3,4))

#
