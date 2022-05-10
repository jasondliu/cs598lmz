import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Test ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# Test ctypes.CFUNCTYPE(ctypes.c_int, None, ctypes.c_int)
ctypes.CFUNCTYPE(ctypes.c_int, None, ctypes.c_int)

# Test ctypes.CFUNCTYPE(None, None, ctypes.c_int)
ctypes.CFUNCTYPE(None, None, ctypes.c_int)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, None)
ctypes.CFUNCTYPE(ctypes.c_int, c
