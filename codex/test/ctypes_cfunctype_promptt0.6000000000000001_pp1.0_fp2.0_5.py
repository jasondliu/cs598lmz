import ctypes
# Test ctypes.CFUNCTYPE
def callback(x):
    return x
cb = ctypes.CFUNCTYPE(ctypes.c_int)(callback)
