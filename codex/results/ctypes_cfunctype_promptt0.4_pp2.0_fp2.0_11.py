import ctypes
# Test ctypes.CFUNCTYPE
def func(arg):
    return arg
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
cmp_func(42)

# Test ctypes.PYFUNCTYPE
def func(arg):
    return arg
CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
cmp_func(42)

# Test ctypes.WINFUNCTYPE
def func(arg):
    return arg
CMPFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
cmp_func(42)

# Test ctypes.CFUNCTYPE with error
def func(arg):
    return arg
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int)
try:
    cmp_func
