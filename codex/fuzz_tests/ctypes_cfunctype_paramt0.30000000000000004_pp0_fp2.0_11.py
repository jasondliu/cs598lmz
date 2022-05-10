import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

cfunc = FUNTYPE(func)

print(cfunc(2))

#%%

import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

def func(p):
    return p.x**2 + p.y**2

cfunc = FUNTYPE(func)

p = Point(2, 3)
print(cfunc(p))

#%%

import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

def func(p):
    return p.x**2 + p.y**2

cfunc = FUNTYPE(func)

p = Point(2, 3)
print(cfunc(p))

#%%

import ctypes

class Point(ctypes.
