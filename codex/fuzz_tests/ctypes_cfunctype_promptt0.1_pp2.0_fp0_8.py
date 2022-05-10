import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype of the function in the dll
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function in the dll
restype = ctypes.c_int
argtypes = (ctypes.c_int,)
func = prototype((restype, argtypes), ((1,), (2,)))

# the function to pass to the dll function
def funcptr(value):
    return value + 1

# call the dll function
res = lib.call_function_pointer(func, funcptr)
if res != 3:
    raise RuntimeError("function pointer call failed")

# call a function with a function pointer argument

# prototype of the function in the dll
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function in the dll
restype = ctypes.
