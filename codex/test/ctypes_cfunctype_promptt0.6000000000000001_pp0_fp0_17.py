import ctypes
# Test ctypes.CFUNCTYPE.
def PYFUNC(*args):
    return ctypes.c_int(42)

