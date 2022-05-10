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

f_c = np.vectorize(f)

print(f_c(2))

#%%
import ctypes
import numpy as np

def f(x):
    return x**2

f_c = np.vectorize(f)

print(f_c(2))

#%%
import ctypes
import numpy as np

def f(x):
    return x**2

f_c = np.vectorize(f)

print(f_c(2))

#%%
import ctypes
import numpy as np

def f(x):
    return x**2

f_c = np.vectorize(f)

print(f_c(2))

#%%
import c
