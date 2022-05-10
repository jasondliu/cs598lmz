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
func.restype = restype
func.argtypes = argtypes

func.errcheck = _ctypes_test.errcheck_int

for i in range(16):
    result = func(i)
    if result != i * 2:
        raise RuntimeError("%d * 2 = %d" % (i, result))

# call a function with a simple argument
# and a simple result, using a function
# pointer

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
restype = ctypes.c_int
argtypes = (ctypes.c
