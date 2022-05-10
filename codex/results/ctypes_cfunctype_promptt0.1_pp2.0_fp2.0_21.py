import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.  It takes a function pointer as
# argument, and calls it.

lib.pass_in_function(CALLBACK(lambda x: x * 5))

# This is the function to call.  It takes a function pointer as
# argument, and calls it.

lib.pass_in_function(CALLBACK(lambda x: x * 7))

# This is the function to call.  It takes a function pointer as
# argument, and calls it.

lib.pass_in_function(CALLBACK(lambda x: x * 9))

# This is the function to call.  It takes a function pointer as
# argument, and calls it.

lib
