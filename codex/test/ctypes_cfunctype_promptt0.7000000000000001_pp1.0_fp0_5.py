import ctypes
# Test ctypes.CFUNCTYPE function type

# test a simple function
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f_paramflags = (1, "i", "")
f_restype = ctypes.c_int
f_argtypes = (ctypes.c_int,)

