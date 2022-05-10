import ctypes
# Test ctypes.CFUNCTYPE()

PCT = ctypes.POINTER(ctypes.c_int)
FPT = ctypes.CFUNCTYPE(PCT)

