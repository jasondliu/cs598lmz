import ctypes
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

class IPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

class Test(ctypes.Structure):
    _fields_ = [("point", Point),
                ("ipoint", IPoint)]

t = Test()
# Simple assignment
t.point = Point(1.0, 2.0, 3.0)
print t.point.x, t.point.y, t.point.z

# Assign a tuple
t.point = 1.0, 2.0, 3.0
print t.point.x, t.point.y, t.point.z

# Assign a list
t.point = [1.0, 2.0, 3.0]
print t.point
