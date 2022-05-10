import ctypes
ctypes.cast(ctypes.byref(ctypes.c_int(1)), ctypes.c_void_p)

# The following should not typecheck because the cast is not needed
ctypes.c_int(1)

# The following should not typecheck because the cast is not needed
ctypes.cast(ctypes.byref(ctypes.c_int(1)), ctypes.c_void_p)
