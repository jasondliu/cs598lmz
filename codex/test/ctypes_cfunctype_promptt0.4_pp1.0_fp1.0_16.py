import ctypes
# Test ctypes.CFUNCTYPE
def py_func(x):
    return x + 1

c_func = ctypes.CFUNCTYPE(ctypes.c_int)(py_func)
