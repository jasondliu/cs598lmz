import ctypes
# Test ctypes.CFUNCTYPE, for functions with no arguments.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Prototype a function that takes no arguments
# and returns a simple integer
prototype = ctypes.CFUNCTYPE(ctypes.c_int)

# Get a pointer to the function
restype = ctypes.c_int
cfunc = prototype((b"one_arg_ret_int", lib))

# Call the function
res = cfunc()

if res != 42:
    raise Exception("one_arg_ret_int() returned %d, should be 42" % res)
