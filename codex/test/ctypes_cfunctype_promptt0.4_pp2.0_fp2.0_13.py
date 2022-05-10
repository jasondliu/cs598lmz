import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

func_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
func_c(1, 2)

# Test ctypes.POINTER

def func(a, b):
    return a + b

