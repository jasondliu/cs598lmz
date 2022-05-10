import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function with a callback parameter
# It calls the callback function with a pointer to a
# structure as argument.  The callback function must
# return the sum of the two integer members of the
# structure.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

restype = ctypes.c_int
argtypes = (prototype, ctypes.c_int)

# The callback function
def func(values):
    return values[0] + values[1]

# The callback function as CFUNCTYPE instance
# The first parameter is the return type, the rest
# the parameter types.

cfunc = prototype(func)

# Call the function in the dll

result = lib.callback(cfunc, 1)
if result != 3:
    raise RuntimeError("callback() returned %d instead of 3" % result)

# Test the errcheck feature

