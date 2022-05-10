import ctypes
# Test ctypes.CFUNCTYPE.

def c_callback(arg1, arg2, arg3):
    return arg1, arg2, arg3


CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

cb_func = CALLBACK(c_callback)
