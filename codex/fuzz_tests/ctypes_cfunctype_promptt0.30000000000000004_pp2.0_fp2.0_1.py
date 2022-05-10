import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print('func', args)
    return args[-1]

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(1, 2))

_ctypes_test.set_cmp_func.argtypes = (CMPFUNC,)
_ctypes_test.set_cmp_func(cmp_func)

print(_ctypes_test.call_cmp_func(1, 2))
