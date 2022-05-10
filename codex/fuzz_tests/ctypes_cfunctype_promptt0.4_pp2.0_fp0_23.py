import ctypes
# Test ctypes.CFUNCTYPE(None)
def func():
    pass

CFUNCTYPE(None)(func)
# Test ctypes.CFUNCTYPE(ctypes.c_int)
def func():
    return 1

CFUNCTYPE(c_int)(func)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(a):
    return a

CFUNCTYPE(c_int, c_int)(func)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(a, b):
    return a + b

CFUNCTYPE(c_int, c_int, c_int)(func)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(a, b, c):
    return a + b + c

CFUNCTYPE(c_int
