import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

def func(*args):
    print(args)

CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

cmp_func = CMPFUNC(func)

lib.set_cmp_func(cmp_func)

lib.call_cmp_func(1, 2)
lib.call_cmp_func(2, 1)

# Test ctypes.PYFUNCTYPE

def py_func(*args):
    print(args)
    return args[0]

PYFUNC = PYFUNCTYPE(c_int, c_int, c_int)

py_func = PYFUNC(py_func)

lib.set_cmp_func(py_func)

lib.call_cmp_func(1, 2)
lib.call_cmp_func(2, 1)

# Test ctypes.WINFUNCTYPE

def win_func(*args):

