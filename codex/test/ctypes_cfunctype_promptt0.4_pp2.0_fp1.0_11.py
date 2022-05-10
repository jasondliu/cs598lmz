import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(*args):
    return args

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

lib.my_qsort.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_int, CMPFUNC)

a = (ctypes.c_int * 10)()
for i in range(len(a)):
    a[i] = 10 - i

lib.my_qsort(a, len(a), ctypes.sizeof(ctypes.c_int), CMPFUNC(func))

for i in range(len(a)):
    assert a[i] == i + 1

##
