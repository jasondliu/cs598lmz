import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def callback(x, y):
    return x + y

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(callback)
print cb(1, 2)

# Test ctypes.byref

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)
print point.x, point.y

ctypes.byref(point).contents.x = 3
ctypes.byref(point).contents.y = 4
print point.x, point.y

# Test ctypes.cast

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)
print point.x, point.y

