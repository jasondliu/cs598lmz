import ctypes
# Test ctypes.CFUNCTYPE
def func(arg):
    return arg

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

cmp_func = CMPFUNC(func)
assert cmp_func(ctypes.pointer(ctypes.c_int(42))) == 42

# Test ctypes.PYFUNCTYPE
def func(arg):
    return arg

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

cmp_func = CMPFUNC(func)
assert cmp_func(ctypes.pointer(ctypes.c_int(42))) == 42

# Test ctypes.WINFUNCTYPE
def func(arg):
    return arg

CMPFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

cmp_func = CMPFUNC(func)
assert cmp_func
