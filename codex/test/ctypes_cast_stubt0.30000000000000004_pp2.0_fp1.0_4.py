import ctypes
ctypes.cast(ctypes.c_void_p(0), ctypes.c_void_p)

# test ctypes.cast(None, ctypes.c_void_p)
ctypes.cast(None, ctypes.c_void_p)

# test ctypes.cast(None, ctypes.c_void_p).value
ctypes.cast(None, ctypes.c_void_p).value

# test ctypes.cast(None, ctypes.c_void_p).value == 0
ctypes.cast(None, ctypes.c_void_p).value == 0

# test ctypes.cast(None, ctypes.c_void_p).value == None
ctypes.cast(None, ctypes.c_void_p).value == None

# test ctypes.cast(None, ctypes.c_void_p) == 0
ctypes.cast(None, ctypes.c_void_p) == 0

# test ctypes.cast(None, ctypes.c_void_p) == None
