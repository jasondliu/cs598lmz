import ctypes
# Test ctypes.CFUNCTYPE
c_int_p = ctypes.POINTER(ctypes.c_int)


def func(p):
    return p[0]


cf = ctypes.CFUNCTYPE(ctypes.c_int)(func)
a = ctypes.c_int(4)
