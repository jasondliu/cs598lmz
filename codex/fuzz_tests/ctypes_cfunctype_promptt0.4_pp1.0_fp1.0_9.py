import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(1, 2)

# Test ctypes.WINFUNCTYPE

def func(a, b):
    return a + b

CMPFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(1, 2)

# Test ctypes.PYFUNCTYPE

def func(a, b):
    return a + b

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(1,
