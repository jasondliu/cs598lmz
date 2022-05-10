import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b",)

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y)]

z = Z()
z.y.x.a = 42
print z.y.x.a

# Test ctypes.Union
class U(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

u = U()
u.a = 42
print u.a, u.b

# Test ctypes.POINTER
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

PS = ctypes.POINTER(S)
ps = PS()
ps.contents = S()
ps.contents.a
