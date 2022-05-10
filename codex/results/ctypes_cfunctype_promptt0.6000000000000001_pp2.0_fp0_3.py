import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x * 2

CFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

f = CFUNC(func)
print(f(4))
