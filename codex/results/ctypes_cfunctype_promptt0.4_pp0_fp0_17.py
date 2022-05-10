import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b, c):
    return a + b + c

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)

print cmp_func(1, 2)
print cmp_func(1, 2, 3)

try:
    cmp_func(1, 2, 3, 4)
except TypeError, details:
    print details

try:
    CMPFUNC(func, 1, 2)
except TypeError, details:
    print details

try:
    CMPFUNC(func, argtypes=(ctypes.c_int, ctypes.c_int))
except TypeError, details:
    print details

try:
    CMPFUNC(func, restype=ctypes.c_int)
except TypeError, details:
    print details

try:
    CMPFUNC(func, use_errno=True)
except TypeError, details:
   
