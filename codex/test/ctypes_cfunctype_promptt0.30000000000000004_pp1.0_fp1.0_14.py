import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(arg):
    return arg

