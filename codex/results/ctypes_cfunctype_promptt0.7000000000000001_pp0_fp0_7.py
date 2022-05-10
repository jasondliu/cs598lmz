import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b, c):
    return a, b, c

func_ptr = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
func_ptr(1, 2, 3)
