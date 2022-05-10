import ctypes
# Test ctypes.CFUNCTYPE(). This is used to create callbacks.

#@<> ctypes.CFUNCTYPE()
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

#@<> ctypes.CFUNCTYPE() - restype
# void
c_void_p = ctypes.CFUNCTYPE(None)
# int
c_int_p = ctypes.CFUNCTYPE(ctypes.c_int)
# int *
c_int_pointer_p = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int))
# long
c_long_p = ctypes.CFUNCTYPE(ctypes.c_long)
# double
c_double_p = ctypes.CFUNCTYPE(ctypes.c_double)
# char *
c_char_pointer_p = ctypes.CFUNCTYPE(ctypes.c_char_p)
# char **
c_char_pointer_pointer_p =
