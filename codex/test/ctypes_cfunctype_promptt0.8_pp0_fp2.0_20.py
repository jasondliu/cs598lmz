import ctypes
# Test ctypes.CFUNCTYPE()

type_a = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@type_a
def func_a(a):
    return a*2

assert func_a(21) == 42
# Test ctypes.CFUNCTYPE() with additional arguments

type_b = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

