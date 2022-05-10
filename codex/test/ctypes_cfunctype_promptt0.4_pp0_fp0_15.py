import ctypes
# Test ctypes.CFUNCTYPE
def func(x):
    return x

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
f(1)

# Test ctypes.PYFUNCTYPE
def func(x):
    return x

f = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
f(1)

# Test ctypes.WINFUNCTYPE
def func(x):
    return x

