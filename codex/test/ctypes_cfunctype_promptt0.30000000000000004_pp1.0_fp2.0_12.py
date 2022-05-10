import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print(args)
    return args

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(1, 2))

# Test ctypes.PYFUNCTYPE

PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

py_func = PYFUNC(func)

print(py_func(1, 2))

# Test ctypes.WINFUNCTYPE

