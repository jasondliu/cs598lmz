import ctypes
# Test ctypes.CField
# ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    def __repr__(self):
        return "<POINT(%d, %d)>" % (self.x, self.y)

p = POINT(10, 20)
print p.x
print p.y

print p

# ctypes.Union
class RECT(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

r = RECT()
print r.a
print r.b
print r.c
print r.d

# ctypes.Union
class POINT2(ctypes.Union):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("xy", ctypes
