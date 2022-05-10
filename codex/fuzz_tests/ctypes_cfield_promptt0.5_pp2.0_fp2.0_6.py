import ctypes
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

p = Point(1, 2)
print(p)
print(p.x, p.y)

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

p = Point(1, 2)
print(p)
print(p.x, p.y)
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

p = Point(1, 2)
print(p)
print(p.x, p.y)


