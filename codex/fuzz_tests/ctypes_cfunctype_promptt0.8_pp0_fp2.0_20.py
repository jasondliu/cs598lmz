import ctypes
# Test ctypes.CFUNCTYPE()

type_a = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@type_a
def func_a(a):
    return a*2

assert func_a(21) == 42
# Test ctypes.CFUNCTYPE() with additional arguments

type_b = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@type_b(4, 5)
def func_b(a, b):
    return a*b

assert func_b(2, 3) == 6
# Test ctypes.CFUNCTYPE() with reentrant call

type_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int)

@type_c
def func_c(a, length):
    return sum(a[:length])

expected = 12345
r = func_c((ctypes.c_
