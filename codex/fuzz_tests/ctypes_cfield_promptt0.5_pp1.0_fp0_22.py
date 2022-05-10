import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

try:
    class Z(X, Y):
        _fields_ = [("z", ctypes.CField)]
except TypeError, details:
    print details

try:
    class Z(X, Y):
        _fields_ = [("z", ctypes.CField(X))]
except TypeError, details:
    print details

class Z(X, Y):
    _fields_ = [("z", ctypes.CField(X, "x"))]

z = Z()
print z.z, z.x
z.z = 1
print z.z, z.x

try:
    class Z(X, Y):
        _fields_ = [("z", ctypes.CField(X, "y"))]
except AttributeError, details:
    print details

try:
    class Z(
