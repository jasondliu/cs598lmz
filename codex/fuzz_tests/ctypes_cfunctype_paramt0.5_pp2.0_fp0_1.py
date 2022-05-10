import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def PyFunc(x):
    return x**2
Cfunc = FUNTYPE(PyFunc)
Cfunc(2)

#%%
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def PyFunc(x):
    return x**2
Cfunc = FUNTYPE(PyFunc)
Cfunc(2)

#%%
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
def PyFunc(x, y):
    return x**2 + y**2
Cfunc = FUNTYPE(PyFunc)
Cfunc(2, 3)

#%%
import ctypes
import numpy as np
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, np.ctypeslib.ndpointer(dtype=np.float64))
def PyFunc(x):
    return np
