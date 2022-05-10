import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)
f_c(2)

#%%
from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')
lib.foo(2)

#%%
from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')
lib.foo.restype = ctypes.c_double
lib.foo(2)

#%%
from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')
lib.foo.argtypes = [ctypes.c_double]
lib.foo.restype = ctypes.c_double
lib.foo(2)

#%%
from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')
lib.foo.argtypes = [ctypes.c_double]
lib.foo.restype = ctypes.c_double
lib.foo.errcheck
