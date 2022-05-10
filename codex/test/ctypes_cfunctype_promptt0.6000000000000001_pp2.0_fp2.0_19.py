import ctypes
# Test ctypes.CFUNCTYPE
c_double_ptr = ctypes.POINTER(ctypes.c_double)
c_double_ptr_ptr = ctypes.POINTER(c_double_ptr)
c_int_ptr = ctypes.POINTER(ctypes.c_int)
c_int_ptr_ptr = ctypes.POINTER(c_int_ptr)

