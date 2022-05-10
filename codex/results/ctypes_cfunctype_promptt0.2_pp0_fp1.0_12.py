import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a simple argument
# and a simple result

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

func = prototype((restype, "func"), argtypes)
func.__doc__ = "func(i) function"

func.restype = restype
func.argtypes = argtypes

lib.set_func_type(func)

for i in range(5):
    result = func(i)
    print(i, result)
    if result != i*2:
        raise Exception("%d != %d" % (result, i*2))

# call a function with a simple argument
# and a simple result, using a prototype
# created from a function type

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_
