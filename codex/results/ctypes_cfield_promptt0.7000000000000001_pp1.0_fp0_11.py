import ctypes
# Test ctypes.CField field accessing

import ctypes.test.test_cfield as test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char * 4),
                ("b", ctypes.c_ubyte * 4),
                ("c", ctypes.c_ubyte * 4)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y)]

# Test accessing a structure
p = X()
p.a[0] = 'H'
p.a[1] = 'e'
p.a[2] = 'l'
p.a[3] = 'o'
p.b[0] = 1
p.b[1] = 2
p.b[2] = 3
p.b[3] = 4
p.c[0] = 10
p.c[1] = 20
p.c[2] = 30
p.c[3] = 40

q =
