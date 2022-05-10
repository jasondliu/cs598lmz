import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
print(CMPFUNC)

cmp_func = CMPFUNC(func)
print(cmp_func)

print(cmp_func(1, 2))

print(type(cmp_func))

print(type(cmp_func) == CMPFUNC)

print(type(func) == CMPFUNC)

print(type(func))

print(type(cmp_func) == type(func))

print(cmp_func.__class__)

print(type(cmp_func).__class__)

print(type(func).__class__)

print(cmp_func.__class__ == type(func).__class__)

print(cmp_func.__class__ == type(cmp_func).__class__)

print(cmp_func.__class__ == type(func
