import ctypes
# Test ctypes.CField.
#f = ctypes.CField(ctypes.c_long, 8)
# Test ctypes.Field.
#f = ctypes.Field(ctypes.c_long, 8)
# Test ctypes.POINTER(ctypes.CFuncPtr).
f = ctypes.POINTER(ctypes.CFuncPtr)
print(str(f))
