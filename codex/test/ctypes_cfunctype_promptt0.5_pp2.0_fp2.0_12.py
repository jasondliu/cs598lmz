import ctypes
# Test ctypes.CFUNCTYPE
def func(x, y):
    return x + y

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)

if cmp_func(1, 2) != 3:
    raise Exception("CFUNCTYPE test failed")

# Test ctypes.c_bool
