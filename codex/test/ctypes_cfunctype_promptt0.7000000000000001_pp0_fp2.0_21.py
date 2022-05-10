import ctypes
# Test ctypes.CFUNCTYPE() function
type_ptr_int = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int))
type_ptr_int()

# Test ctypes.cast() function
