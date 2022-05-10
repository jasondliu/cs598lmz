import ctypes
# Test ctypes.CFUNCTYPE(...)
cfunc = ctypes.CFUNCTYPE(ctypes.c_int)((lambda x: x % 2))
# Test C function
