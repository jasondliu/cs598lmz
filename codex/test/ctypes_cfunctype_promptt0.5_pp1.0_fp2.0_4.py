import ctypes
# Test ctypes.CFUNCTYPE
def func(a):
    return a

CFUNCTYPE_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
assert CFUNCTYPE_func(1) == 1

# Test ctypes.POINTER
