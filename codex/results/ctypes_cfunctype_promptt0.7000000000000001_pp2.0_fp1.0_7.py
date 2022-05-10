import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: 1)(None)
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: 1)(1)
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: 1)(1.0)
# Test ctypes.CFUNCTYPE(ctypes.c_float)(lambda x: 1.0)(None)
# Test ctypes.CFUNCTYPE(ctypes.c_float)(lambda x: 1.0)(1)
# Test ctypes.CFUNCTYPE(ctypes.c_float)(lambda x: 1.0)(1.0)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: 1)(0)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: 1)(1)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: 1)(1.
