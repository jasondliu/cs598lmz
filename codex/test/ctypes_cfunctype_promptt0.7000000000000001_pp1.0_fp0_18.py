import ctypes
# Test ctypes.CFUNCTYPE
def func_ptr(x):
    return x + 1
func_ptr_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
func = func_ptr_type(func_ptr)
