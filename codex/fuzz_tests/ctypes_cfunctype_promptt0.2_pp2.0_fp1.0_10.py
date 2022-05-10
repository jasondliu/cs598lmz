import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# this callback receives an integer argument and returns an integer
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the callback implementation
def py_cmp_func(x):
    print("py_cmp_func", x)
    return -x

# the callback wrapper
def cmp_func(x):
    print("cmp_func", x)
    return py_cmp_func(x)

# the callback wrapper as CFUNCTYPE instance
cmp_func_c = CMPFUNC(cmp_func)

# call the function with the callback
res = lib.use_cmp_func(cmp_func_c, 42)
print(res)

# call a function with a callback argument

# this callback receives an integer argument and returns an integer
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int,
