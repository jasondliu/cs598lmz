import ctypes
# Test ctypes.CField

import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class PointPtr(ctypes.POINTER(Point)):
    _type_ = Point

class PointPtrPtr(ctypes.POINTER(PointPtr)):
    _type_ = PointPtr

p = Point()
pp = PointPtr()
ppp = PointPtrPtr()

print Point._fields_
print PointPtr._fields_
print PointPtrPtr._fields_
print

print p._fields_
print pp._fields_
print ppp._fields_
