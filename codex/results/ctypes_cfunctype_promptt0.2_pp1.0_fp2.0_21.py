import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
print f(1, 2)

# Test ctypes.PYFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
print f(1, 2)

# Test ctypes.WINFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CMPFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
print f(1, 2)

