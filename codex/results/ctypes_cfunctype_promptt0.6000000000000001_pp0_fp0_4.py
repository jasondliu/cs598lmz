import ctypes
# Test ctypes.CFUNCTYPE().

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Get a function pointer from the DLL
func = lib.getfunc(functype)

# Call the function
print func(1)

# Create a new function object
newfunc = functype(func)

# Call the function
print newfunc(2)
