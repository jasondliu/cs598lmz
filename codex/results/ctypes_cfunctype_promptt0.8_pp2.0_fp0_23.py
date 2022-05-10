import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_int)
def func(a):
    return a

print(func(1))
