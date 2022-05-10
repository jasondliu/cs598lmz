import ctypes
# Test ctypes.CFUNCTYPE
def func(x):
    return x + 1

cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
print(cfunc(2))
# Test ctypes.POINTER
