import ctypes
# Test ctypes.CFUNCTYPE
c_test1 = ctypes.CFUNCTYPE(ctypes.c_int)(lambda x, y: x + y)
