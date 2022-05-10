import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x, y):
    return x + y

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(1, 2)

print cmp_func.__name__

print cmp_func.__doc__

print cmp_func.__module__

print cmp_func.__dict__

print cmp_func.__class__

print cmp_func.__closure__

print cmp_func.__code__

print cmp_func.__defaults__

print cmp_func.__globals__

print cmp_func.__name__

print cmp_func.__self__

print cmp_func.__weakref__

print cmp_func.func_closure

print cmp_func.func_code

print cmp_func.func_defaults

print
