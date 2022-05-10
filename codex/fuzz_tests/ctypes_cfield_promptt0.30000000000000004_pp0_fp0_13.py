import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y)]

z = Z()
z.x.a = 1
z.x.b = 2
z.y.c = 3
z.y.d = 4

print z.x.a, z.x.b, z.y.c, z.y.d

# Test ctypes.CField.from_address

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int),

