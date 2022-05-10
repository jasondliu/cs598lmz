import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert cfunc(1, 2) == 3

# Test ctypes.PYFUNCTYPE

def func(a, b):
    return a + b

cfunc = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert cfunc(1, 2) == 3

# Test ctypes.WINFUNCTYPE

def func(a, b):
    return a + b

cfunc = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert cfunc(1, 2) == 3

# Test ctypes.CFUNCTYPE with a list of argument types

def func(a, b):
    return a + b

cfunc = ctypes
