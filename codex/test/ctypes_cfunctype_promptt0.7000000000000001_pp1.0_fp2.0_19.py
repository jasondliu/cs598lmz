import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 1)()
print(ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 1)())
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 2)()
print(ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 2)())
