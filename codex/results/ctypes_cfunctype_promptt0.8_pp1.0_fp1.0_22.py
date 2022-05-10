import ctypes
# Test ctypes.CFUNCTYPE

f = ctypes.CFUNCTYPE(ctypes.c_float)(lambda x: x + 1.0)
if f(4) != 5.0:
    raise Exception("Test failed")
