import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

int_func = ctypes.CFUNCTYPE(ctypes.c_int,
                            ctypes.c_int, ctypes.c_int)(func)

assert int_func(1, 2) == 3

