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

func.errcheck = ctypes.default_errcheck

lib.set_func.argtypes = (ctypes.c_void_p,)
lib.set_func(func)

for i in range(5):
    result = lib.call_func(i)
    print(result)
    assert result == i * 2

# call a function with a simple argument
# and a simple result, but the function
# returns a pointer

prototype = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int), ctypes
