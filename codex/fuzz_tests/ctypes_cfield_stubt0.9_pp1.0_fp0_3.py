import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

import sys

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

pt = POINT(10, 20)
print(pt.x, pt.y)
print(bool(pt))
print()

pt = POINT(0, 0)
print(pt.x, pt.y)
print(bool(pt))
print()

pt = POINT(-1, -1)
print(pt.x, pt.y)
print(bool(pt))
print()

print('END')
