import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)(1)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)(1)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)(1)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)(1)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)(1)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x
