import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is a simple C callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is a C function that takes a callback function as an argument
