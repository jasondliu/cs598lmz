import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x, y):
    return x + y

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
print f(1, 2)

# Test ctypes.PYFUNCTYPE

import ctypes

def func(x, y):
    return x + y

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
print f(1, 2)

# Test ctypes.PYFUNCTYPE with exception

import ctypes

def func(x, y):
    raise ValueError

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
try:
    f
