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
func = prototype((restype, argtypes))

# the function to pass as argument
def funcptr(value):
    return value + 1

# call the function in the dll
result = lib.call_function_pointer(func, funcptr, 1)
if result != 3:
    raise Exception("function pointer call failed")

# call a function with a function pointer argument

# prototype of the function in the dll
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function in the dll
restype = ctypes.c_int
argtypes = (
