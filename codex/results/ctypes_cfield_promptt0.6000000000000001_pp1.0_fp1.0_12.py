import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = POINT(1, 2)
print(point.x, point.y)

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    def __init__(self, x=1, y=2):
        self.x = x
        self.y = y

point = POINT()
print(point.x, point.y)

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    def __init__(self, x=1, y=2):
        self.x = x
        self.y = y

point = Point()
