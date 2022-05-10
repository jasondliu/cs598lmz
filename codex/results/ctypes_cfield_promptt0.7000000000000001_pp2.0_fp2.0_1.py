import ctypes
# Test ctypes.CField
# https://docs.python.org/3.4/library/ctypes.html#ctypes.CField
# https://docs.python.org/3.4/library/ctypes.html#ctypes._Union_CField

class Point(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

class Point2(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

class TestUnion(ctypes.Union):
    _fields_ = [
        ('integer', ctypes.c_int),
        ('point', Point),
        ('point2', Point2),
    ]

test = TestUnion()
test.point.x = 1
test.point.y = 2
print(test.point.x, test.point.y)

test.point2.x = 3
test.point2.y = 4
print(test.
