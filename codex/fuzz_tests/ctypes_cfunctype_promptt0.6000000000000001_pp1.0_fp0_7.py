import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
print(ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p))
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
print(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p))

# Test ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
print(ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p))
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
