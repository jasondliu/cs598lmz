import ctypes
# Test ctypes.CFUNCTYPE
CFUNCTYPE = ctypes.CFUNCTYPE

@CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(a, b):
    return a + b

