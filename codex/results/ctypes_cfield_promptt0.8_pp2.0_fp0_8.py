import ctypes
# Test ctypes.CField

import ctypes
class X(ctypes.Structure):
    _fields_ = [("x1", ctypes.c_int),
                ("x2", ctypes.c_int)]

print X.x1
print X.x2
print X().x1
print X().x2

class X(ctypes.Structure):
    _fields_ = [("x1", ctypes.c_int),
                ("x2", ctypes.c_int)]

    _anonymous_ = ["x1"]

print X.x2
print X().x2

# test Field with default value

class X(ctypes.Structure):
    _fields_ = [("x1", ctypes.c_int, 1),
                ("x2", ctypes.c_int, 2)]
print X().x1
print X().x2

# test Field with offset

class X(ctypes.Structure):
    _fields_ = [("x1", ctypes.c_int, 1, 0),
                ("x2", ctypes.c_int,
