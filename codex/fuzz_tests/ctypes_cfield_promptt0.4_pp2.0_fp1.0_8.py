import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("d", ctypes.c_int)]

z = Z()
z.y.x.a = 1
z.y.x.b = 2
z.y.c = 3
z.d = 4

# Test ctypes.CField.from_address
class X2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y2(ctypes.Structure):
    _fields_ = [("x", X2),
                ("c", ctypes.c_int)]

class Z2(ctypes.Structure):
    _fields_
