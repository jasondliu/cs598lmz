import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

p = POINT()
print(p.x, p.y, p.z)

p.x, p.y, p.z = 4, 5, 6
print(p.x, p.y, p.z)

p = POINT(1, 2, 3)
print(p.x, p.y, p.z)

# Test ctypes.CData
class POINT2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

p = POINT2()
print(type(p))
cp = ctypes.pointer(p)
print(type(cp))
cp2 = cp.contents
print(type(cp2))
print(cp2.x, cp2
