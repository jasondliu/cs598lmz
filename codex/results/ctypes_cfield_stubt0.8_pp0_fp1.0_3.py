import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert(isinstance(S.x, ctypes.CField))

import _testcapi

class S2(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_float),
    ]

class S3(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_ubyte),
        ('y', ctypes.c_ushort),
    ]

class S4(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_ubyte),
        ('y', ctypes.c_ushort),
    ]

class T(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_ubyte),
        ('y', ctypes.c_ushort),
    ]

for s in S2, S3, S4:
    # test sizeof()
    assert s.x.offset == 0
    assert s.y.offset == c
