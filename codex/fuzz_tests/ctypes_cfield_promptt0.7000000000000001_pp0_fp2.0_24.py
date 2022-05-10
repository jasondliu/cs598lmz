import ctypes
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class SPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class Line(ctypes.Structure):
    _fields_ = [("p1", Point),
                ("p2", Point)]

class SLine(ctypes.Structure):
    _fields_ = [("p1", SPoint),
                ("p2", SPoint)]

l = Line(Point(1,2), Point(3,4))
sl = SLine(SPoint(1,2), SPoint(3,4))
print(l.p1.x)
print(l.p2.x)
print(sl.p1.x)
print(sl.p2.x)

# Test ctypes.CFuncPtr
libc = ctypes.CDLL("libc.so.6")
atoi =
