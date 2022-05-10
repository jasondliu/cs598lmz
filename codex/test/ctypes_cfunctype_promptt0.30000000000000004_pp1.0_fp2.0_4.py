import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x):
    return x+1

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

assert callback(1) == 2

# Test ctypes.WINFUNCTYPE

import ctypes

def func(x):
    return x+1

