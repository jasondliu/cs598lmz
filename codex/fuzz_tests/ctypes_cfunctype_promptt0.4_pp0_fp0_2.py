import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

assert FUNC(1, 2) == 3

# Test ctypes.WINFUNCTYPE
def func(a, b):
    return a + b

FUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

assert FUNC(1, 2) == 3

# Test ctypes.PYFUNCTYPE
def func(a, b):
    return a + b

FUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

assert FUNC(1, 2) == 3

# Test ctypes.CFUNCTYPE with multiple arguments
def func(a, b, c, d):
    return a + b + c + d

FUN
