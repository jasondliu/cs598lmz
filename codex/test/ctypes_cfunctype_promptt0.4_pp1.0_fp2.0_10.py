import ctypes
# Test ctypes.CFUNCTYPE

# Test ctypes.CFUNCTYPE(None)
# This is a special case, because ctypes.CFUNCTYPE(None) is the same
# as ctypes.CFUNCTYPE(ctypes.c_int)

f = ctypes.CFUNCTYPE(None)
