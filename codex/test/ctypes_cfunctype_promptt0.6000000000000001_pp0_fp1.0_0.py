import ctypes
# Test ctypes.CFUNCTYPE()
get_name = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)
get_name(1)

# Test ctypes.POINTER()
get_name = ctypes.POINTER(get_name)
