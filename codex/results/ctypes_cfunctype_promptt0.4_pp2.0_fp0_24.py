import ctypes
# Test ctypes.CFUNCTYPE

@CFUNCTYPE(c_int, c_int)
def func(n):
    return n * 5

assert func(2) == 10
