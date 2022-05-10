import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

import _ctypes_test
lib = CDLL(_ctypes_test.__file__)

CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int))

def check(n, exp):
    array = (c_int * n)()
    for i in range(len(array)):
        array[i] = i
    qsort = lib.my_qsort
    qsort.argtypes = c_void_p, c_int, c_int, CMPFUNC
    qsort.restype = None

    res = []
    def func(a, b):
        res.append((a[0], b[0]))
        return a[0] - b[0]

    qsort(array, len(array), sizeof(c_int), CMPFUNC(func))
    assert res == exp

check(1, [])
check(2, [(0, 1)])
check(3, [(0, 1),
