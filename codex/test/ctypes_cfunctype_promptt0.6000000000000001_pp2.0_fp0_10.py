import ctypes
# Test ctypes.CFUNCTYPE()
print(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))
# Test ctypes.POINTER()
print(ctypes.POINTER(ctypes.c_int))

# Test ctypes.cast()
