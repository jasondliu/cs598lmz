import ctypes
# Test ctypes.CFUNCTYPE()

def func(a, b, c):
    print a, b, c

FUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

FUNC(1, 2, 3)

# Test ctypes.Structure()

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = Point(1, 2)
print p.x, p.y

# Test ctypes.POINTER()

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

PointPtr = ctypes.POINTER(Point)

p = Point(1, 2)
pp = PointPtr(p)
print pp.contents.x, pp.contents.y

# Test ctypes.c_char_p()

s = ctypes.
