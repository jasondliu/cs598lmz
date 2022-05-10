import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(X), ctypes.POINTER(Y))

def compare(x, y):
    print("compare", x.contents, y.contents)
    return x.contents.a - y.contents.a

cmp_func = CMPFUNC(compare)

lib.set_qsort_compare(cmp_func)

a = (X * 3)(X(1, 2), X(3, 4), X(5, 6))
lib.do_qsort(a, 3)


