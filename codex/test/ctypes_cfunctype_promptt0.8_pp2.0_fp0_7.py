import ctypes
# Test ctypes.CFUNCTYPE
cbifunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x * 3)
assert cbifunc(3) == 9
# Test ctypes.WINFUNCTYPE
