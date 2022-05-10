import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is the prototype of the callback function
# int __stdcall callback(int a, int b)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

