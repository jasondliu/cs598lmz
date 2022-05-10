import ctypes
# Test ctypes.CFUNCTYPE
def callback(x):
    return x

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(callback)

