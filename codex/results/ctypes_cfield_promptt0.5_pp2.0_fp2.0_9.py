import ctypes
# Test ctypes.CField with a simple structure.

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [("c", C), ("d", D)]

e = E()
e.c.x = 42
e.d.y = 43
print e.c.x, e.d.y

C._fields_ = [("y", ctypes.c_int)]
e.c.y = 44
print e.c.y, e.c.x

C._fields_ = [("x", ctypes.c_int)]
e.c.x = 45
print e.c.y, e.c.x

print e.c._fields_

e.c.x = 46
print e.c.y, e.c.x
print e.c._fields_

C._fields_ = [("z", ctypes.c
