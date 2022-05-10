import ctypes
# Test ctypes.CFUNCTYPE

def f(x):
    return x

F = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f2 = F(f)

