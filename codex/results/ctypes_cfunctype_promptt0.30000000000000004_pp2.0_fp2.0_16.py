import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

libc = ctypes.CDLL(None)

def func(x):
    return x + 1

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(1)

print cmp_func.__name__
print cmp_func.__doc__
print cmp_func.__module__

# Test ctypes.c_int.from_param
import ctypes

def func(x):
    return x + 1

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(1)

print cmp_func.__name__
print cmp_func.__doc__
print cmp_func.__module__

# Test ctypes.c_int.from_param
import ctypes

def func(x):
