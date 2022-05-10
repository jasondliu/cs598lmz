import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print('func', args)
    return args[-1]

CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFuncPtr(func)

assert cfunc(1, 2) == 2
assert cfunc(3, 4, 5) == 5

# Test ctypes.WINFUNCTYPE

CMPFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
def func(a, b):
    print('func', a, b)
    return 0
cmp_func = CMPFUNC(func)

_ctypes_test.set_cmp_func(cmp_func)
_ctypes_test.call_cmp_func()

# Test ctypes.PYFUNCTYPE

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_
