import ctypes
# Test ctypes.CFUNCTYPE
def f(i, j):
    return i * j
cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(f)
print(cf(4, 5))
ctypes.cast(cf, ctypes.c_void_p)
