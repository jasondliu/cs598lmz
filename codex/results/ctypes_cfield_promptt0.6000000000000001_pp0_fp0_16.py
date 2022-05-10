import ctypes
# Test ctypes.CField

#
# Test ctypes.CField
#

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ubyte, 4),
                ("b", ctypes.c_ubyte, 2),
                ("c", ctypes.c_ubyte, 2)]

class Y(ctypes.Union):
    _fields_ = [("i", ctypes.c_ulong),
                ("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y)]

a = Z()
a.y.x.a = 0x0a
a.y.x.b = 0x02
a.y.x.c = 0x01
print a.y.i
print a.y.x.a
print a.y.x.b
print a.y.x.c

print Z.y.i
print Z.y.x.a
print Z.y.x.b
print Z.y.x.c

print Z.y.i.
