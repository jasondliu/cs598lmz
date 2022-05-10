import ctypes
# Test ctypes.CFUNCTYPE(...)(...).
print(ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x)(3))
# Test ctypes._CFuncPtr(...).
