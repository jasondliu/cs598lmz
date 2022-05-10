import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# the function pointer type
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function
