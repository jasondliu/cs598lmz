import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

cf = FUNTYPE(f)

print(cf(1.0))

#%%
import ctypes
import numpy as np

c_double_p = ctypes.POINTER(ctypes.c_double)

def f(x):
    return x**2

cf = FUNTYPE(f)

x = np.linspace(0, 1, 10)
cf_vec = np.vectorize(cf)
print(cf_vec(x))

#%%
import ctypes
import numpy as np

c_double_p = ctypes.POINTER(ctypes.c_double)

def f(x):
    return x**2

cf = FUNTYPE(f)

x = np.linspace(0, 1, 10)
cf_vec = np.vectorize(cf)
print(cf_vec(x))

#%%
import ctypes
import numpy as np

c_double_p = c
