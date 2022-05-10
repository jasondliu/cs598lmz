import ctypes
# Test ctypes.CFUNCTYPE

f = ctypes.CFUNCTYPE(ctypes.c_float)(lambda x: x + 1.0)
