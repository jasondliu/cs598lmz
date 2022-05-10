import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
