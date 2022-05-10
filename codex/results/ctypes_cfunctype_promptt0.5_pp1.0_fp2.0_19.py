import ctypes
# Test ctypes.CFUNCTYPE
@cfunc(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))
def f(x):
    return x

assert f(3) == 3
# Test ctypes.PYFUNCTYPE
@cfunc(ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int))
def f(x):
    return x

assert f(3) == 3
# Test ctypes.WINFUNCTYPE
@cfunc(ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int))
def f(x):
    return x

assert f(3) == 3
# Test ctypes.CFUNCTYPE.in_dll
@cfunc(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))
def f(x):
    return x

f.in_dll(ctypes, "f")
assert ctypes.f(3) == 3
# Test ctypes.PYFUNCTYPE
