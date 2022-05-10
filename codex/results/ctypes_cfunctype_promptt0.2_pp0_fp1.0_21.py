import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer as argument

def func(x):
    return x + 42

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

res = lib.pass_func(callback)
if res != func(0):
    raise RuntimeError("function pointer call failed")

# call a function with a function pointer as argument

def func(x):
    return x + 42

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

res = lib.pass_func(callback)
if res != func(0):
    raise RuntimeError("function pointer call failed")

# call a function with a function pointer as argument

def func(x):
    return x + 42

CALLBACK = ctypes.CFUNCTYPE(
