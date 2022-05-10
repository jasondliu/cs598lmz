import ctypes
# Test ctypes.CFUNCTYPE
def foo(x, c):
    c.value = c.value * 2
    return x * 2

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))(foo)
c = ctypes.c_int(12)
