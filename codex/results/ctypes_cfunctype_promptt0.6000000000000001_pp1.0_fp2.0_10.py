import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(x):
    return x * 2

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# convert the Python function into a C function pointer
cfunc = CALLBACKFUNC(func)

# pass the function pointer to a C callback function
res = lib.callback(cfunc, 1, 2)
print(res)

# convert the C function pointer back into a Python function
pyfunc = cfunc.in_dll(lib, 'callback')
print(pyfunc)

res = pyfunc(1, 2)
print(res)

# test that the pointer can be used several times
res = lib.callback(cfunc, 2, 4)
print(res)

res = lib.callback(cfunc, 3, 6)
print(res)

# test that the function pointer is really callable
res = cfunc(3)
print(res)

#
