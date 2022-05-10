import ctypes
# Test ctypes.CFUNCTYPE
i = 123
c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda i: i + 1)
