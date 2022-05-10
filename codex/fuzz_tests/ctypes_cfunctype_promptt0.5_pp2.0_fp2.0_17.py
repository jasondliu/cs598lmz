import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# ctypes.c_int.from_param(i)

# ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(i)

# ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))(i)

# ctypes.cast(i, ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)))

# ctypes.cast(i, ctypes.c_void_p).value

# ctypes.cast(i, ctypes.c_void_p).value == i

# ctypes.cast(i, ctypes.c_void_p).value == ctypes.cast(i, ctypes.c_void_p)

# ctypes.cast(i, ctypes.c_void_p).value == ctypes.cast(i, ctypes.c_void_p).value

# ctypes
