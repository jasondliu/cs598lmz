import ctypes
# Test ctypes.CFUNCTYPE.
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float, ctypes.c_float)(lambda f1, f2: f1
    < f2)
func(1.1, 2.0)


