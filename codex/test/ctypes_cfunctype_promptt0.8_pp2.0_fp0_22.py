import ctypes
# Test ctypes.CFUNCTYPE
def f(x):
    return 2*x

g = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)
assert g(2) == 4
# Test ctypes.POINTER
g2 = ctypes.POINTER(ctypes.c_int)
