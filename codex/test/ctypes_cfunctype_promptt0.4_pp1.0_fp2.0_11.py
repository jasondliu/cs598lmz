import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b, c):
    return a + b + c
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
