import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
lib.my_test_1.restype = restype

lib.my_test_1.argtypes = (ctypes.c_int,)

for i in range(1, 10):
    func = lib.my_test_1(i)
    res = func(i)
    if res != i:
        raise RuntimeError("%d != %d" % (res, i))

for i in range(1, 10):
    func = lib.my_test_1(i)
    res = func(i)
    if res != i:
        raise RuntimeError("%d != %d" % (res, i))

# Test ctypes.CFUNCTYPE with a structure as restype

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
               
