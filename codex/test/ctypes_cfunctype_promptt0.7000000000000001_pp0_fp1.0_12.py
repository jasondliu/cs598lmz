import ctypes
# Test ctypes.CFUNCTYPE

func = ctypes.CFUNCTYPE(ctypes.c_double)(lambda x: x+1)
