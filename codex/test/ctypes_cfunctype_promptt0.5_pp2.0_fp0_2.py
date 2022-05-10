import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

# Test ctypes.POINTER
