import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2)
    y = ctypes.c_double(3)
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

class Point3D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

