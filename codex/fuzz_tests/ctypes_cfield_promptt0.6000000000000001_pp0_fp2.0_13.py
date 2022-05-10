import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)
print("point.x =", point.x)
print("point.y =", point.y)

# Test ctypes.CArray
class POINTS(ctypes.Structure):
    _fields_ = [("points", ctypes.c_int * 3)]

points = POINTS((1, 2, 3))
print("points.points =", points.points)

class POINTS2(ctypes.Structure):
    _fields_ = [("points", ctypes.c_int * 3)]

points2 = POINTS2((1, 2, 3))
print("points2.points =", points2.points)

# Test ctypes.CStruct
class POINT3(ctypes.Structure):
    _fields_ = [("point", ctypes.c_int * 3)]

point3 = POINT3((1, 2
