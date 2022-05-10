import ctypes
# Test ctypes.CFields/CFieldsRef

C_FLOAT = ctypes.c_float

# The C type definitions
class Point(ctypes.Structure):
    _fields_ = [("x", C_FLOAT),
                ("y", C_FLOAT)]

class Line(ctypes.Structure):
    _fields_ = [("start", Point),
                ("stop", Point)]


# Playing around in pure python
p = Point(1.0, 2.0)
print(p)

pp = Point.x(p)
print(pp)

l = Line(p, pp)
print(l)
# Test ctypes.CFields/CFieldsRef

C_FLOAT = ctypes.c_float

# The C type definitions
class Point(ctypes.Structure):
    _fields_ = [("x", C_FLOAT),
                ("y", C_FLOAT)]

class Line(ctypes.Structure):
    _fields_ = [("start", Point),
                ("stop", Point)]


# Playing
