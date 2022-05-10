import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple function

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

paramflags = (1, "x")

restype = ctypes.c_int

argtypes = (ctypes.c_int,)

functype = ctypes.CFUNCTYPE(restype, *argtypes)

func = functype((prototype, "simple_function", paramflags),
                (lib, "simple_function"))

print func(42)

# a function with a pointer parameter

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

paramflags = (1, "x")

restype = ctypes.c_int

argtypes = (ctypes.POINTER(ctypes.c_int),)

functype = ctypes.CFUNCTYPE(restype, *
