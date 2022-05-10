import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(*args):
    return args

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This function is in _ctypes_test.c
lib.my_qsort.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_int, CMPFUNC)
lib.my_qsort.restype = None

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

a = (POINT * 5)()
a[0].x = 1
a[1].x = 5
a[2].x = 3
a[3].x = 2
a[4].x = 4

lib.my_qsort(a, len(a), ctypes.sizeof(PO
