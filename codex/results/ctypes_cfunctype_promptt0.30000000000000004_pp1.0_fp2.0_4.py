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

CALLBACK = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

assert callback(1) == 2

# Test ctypes.PYFUNCTYPE

import ctypes

def func(x):
    return x+1

CALLBACK = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

assert callback(1) == 2

# Test ctypes.CFUNCTYPE with a string

import ctypes

def func(x):
    return x+1

