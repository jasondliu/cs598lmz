import ctypes
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = Point(1, 2)
p.y = 3
print(p.y)
print(p.x)
