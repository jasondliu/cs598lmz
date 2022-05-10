import ctypes
# Test ctypes.CFUNCTYPE()

# This is the prototype of the callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# This is the function that will be called by the callback
