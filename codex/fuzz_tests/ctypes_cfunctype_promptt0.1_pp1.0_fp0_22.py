import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.  It takes a function pointer as
# argument, and calls it.

lib.pass_in_function(CALLBACKFUNC(lambda x: x * 5))

# This is a function that returns a function pointer.

lib.return_function.restype = CALLBACKFUNC

# Call the function, and call the function pointer it returns.

lib.return_function()(6)

# This is a function that takes a function pointer as argument.
# The function pointer must have no arguments, and returns
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int)

# This is the
