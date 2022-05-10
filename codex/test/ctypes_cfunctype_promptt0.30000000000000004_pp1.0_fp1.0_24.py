import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call_function takes a function pointer and an integer argument.  It
# calls the function with the integer argument and returns the result
