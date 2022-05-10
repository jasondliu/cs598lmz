import ctypes
# Test ctypes.CFUNCTYPE

# This is the prototype of the callback function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

