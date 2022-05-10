import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

assert FUNC(1, 2) == 3

# Test ctypes.WINFUNCTYPE
def func(a, b):
    return a + b

