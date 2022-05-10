import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print("callback called with", x)
    return x

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

