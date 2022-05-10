import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)
f_c(2)

#%%
# function pointer
def f(x):
    return x**2

f_c = ctypes.cast(f, FUNTYPE)
f_c(2)

#%%
# function pointer
def f(x):
    return x**2

f_c = ctypes.cast(f, FUNTYPE)
f_c(2)

#%%
# function pointer
def f(x):
    return x**2

f_c = ctypes.cast(f, FUNTYPE)
f_c(2)

#%%
# function pointer
def f(x):
    return x**2

f_c = ctypes.cast(f, FUNTYPE)
f_c(2)

#%%
# function pointer
def f(x):
    return x**2

f_c = ctypes.cast(f, FUNTYPE)
f
