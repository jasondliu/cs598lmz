import ctypes
# Test ctypes.CFUNCTYPE()

def C(x):
    return x+1

# ref: https://docs.python.org/2/library/ctypes.html#callback-functions
C = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(C)

