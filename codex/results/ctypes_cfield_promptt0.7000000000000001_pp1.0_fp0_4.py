import ctypes
# Test ctypes.CField
f = ctypes.CField(ctypes.c_int)
f.offset
f.name
f.ctype
class Point(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)]

Point._fields_
class Point(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)]

Point._fields_
class Point(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)]

Point._fields_
Point._fields_
# Test ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)]

Point._fields_
p = Point()
p.x
p.y
p.x = 1
p.y = 2

