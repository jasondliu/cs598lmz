import ctypes
# Test ctypes.CFUNCTYPE()
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cfunc = CMPFUNC(func)

print(cfunc(1, 2))

# Test ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

point = Point()
point.x = 1
point.y = 2

print(point.x, point.y)
# Test ctypes.POINTER()
point_pointer = ctypes.POINTER(Point)

point1 = Point()
point1.x = 3
point1.y = 4

point2 = Point()
point2.x = 5
point2.y = 6

array = (point1, point2)

print(array[0].x, array[0].y)
