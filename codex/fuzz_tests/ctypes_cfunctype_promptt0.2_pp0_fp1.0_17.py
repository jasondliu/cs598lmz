import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x):
    print("func", x)
    return x * 2

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

print(callback(2))

# Test ctypes.PYFUNCTYPE

import ctypes

def func(x):
    print("func", x)
    return x * 2

CALLBACK = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

print(callback(2))

# Test ctypes.WINFUNCTYPE

import ctypes

def func(x):
    print("func", x)
    return x * 2

CALLBACK = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

print(callback(2))

# Test ctypes.CFUNCTYPE with
