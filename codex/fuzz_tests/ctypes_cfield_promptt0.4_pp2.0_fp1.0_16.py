import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint32, 1),
                ("b", ctypes.c_uint32, 2),
                ("c", ctypes.c_uint32, 3),
                ("d", ctypes.c_uint32, 4),
                ("e", ctypes.c_uint32, 5),
                ("f", ctypes.c_uint32, 6),
                ("g", ctypes.c_uint32, 7),
                ("h", ctypes.c_uint32, 8)]

x = X()
print x.a
print x.b
print x.c
print x.d
print x.e
print x.f
print x.g
print x.h

# Test ctypes.CField.from_param
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint32, 1),
                ("b", ctypes.c_uint32, 2),
                ("c", ctypes.c_uint32, 3),

