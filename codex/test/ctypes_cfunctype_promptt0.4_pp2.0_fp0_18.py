import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x):
    print("x =", x)
    return x + 1

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

func_var = func_type(func)

print(func_var(1))

# Test ctypes.WINFUNCTYPE

import ctypes

def func(x):
    print("x =", x)
    return x + 1

