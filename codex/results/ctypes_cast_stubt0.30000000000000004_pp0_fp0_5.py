import ctypes
ctypes.cast(ctypes.pointer(c_int(42)), ctypes.POINTER(ctypes.c_double))

# Convert from ctypes instance to buffer compatible object
buf = ctypes.cast(ctypes.pointer(c_int(42)), ctypes.c_void_p).value

# Convert from buffer compatible object to ctypes instance
ctypes.cast(ctypes.c_void_p(buf), ctypes.POINTER(ctypes.c_int))

# Convert from ctypes instance to buffer compatible object
buf = ctypes.cast(ctypes.pointer(c_int(42)), ctypes.c_void_p).value

# Convert from buffer compatible object to ctypes instance
ctypes.cast(ctypes.c_void_p(buf), ctypes.POINTER(ctypes.c_int))

# Convert from ctypes instance to buffer compatible object
buf = ctypes.cast(ctypes.pointer(c_int(42)), ctypes.c_void_p).value

# Convert from buffer compatible object to ctypes instance
ctypes.cast(ctypes.c_void
