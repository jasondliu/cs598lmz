import ctypes
# Test ctypes.CFUNCTYPE 

# TypeError: cannot be converted to a pointer
# callback = ctypes.CFUNCTYPE(None)

# TypeError: cannot be converted to a pointer
# callback = ctypes.CFUNCTYPE(ctypes.c_void_p)

# TypeError: cannot be converted to a pointer
# callback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

# TypeError: cannot be converted to a pointer
# callback = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

# TypeError: cannot be converted to a pointer
# callback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

# TypeError: cannot be converted to a pointer
# callback = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

# TypeError: cannot be converted to a pointer
# callback = c
