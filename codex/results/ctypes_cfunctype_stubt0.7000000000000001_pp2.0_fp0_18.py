import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun()

@jit
def f(x):
    return x+1
f(2)

@jit
def f(x):
    return x+1
f(3)

x = np.random.rand(100,100)
y = np.random.rand(100,100)

@jit
def add(x,y):
    return x+y

import numba
@numba.jit
def add(x,y):
    return x+y

%timeit add(x,y)

@numba.jit
def add(x,y):
    return x+y

%timeit add(x,y)

@numba.jit("void(f8[:,:],f8[:,:])")
def add(x,y):
    return x+y

%timeit add(x,y)

@numba.jit("void(f8[:,:],f8[:,:],f8[:,:])")
def add(x,y,z):
    for
