import ctypes
# Test ctypes.CField in a structure
class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class D(C):
    _fields_ = [("z", ctypes.c_int)]

d = D(1, 2, 3)
print(d.x, d.y, d.z)

print(D.x)

print(D.y)

print(D.z)

print(D.y.offset)

print(D.z.offset)

print(D.z.offset - D.y.offset)

print(D.z.offset - D.x.offset)

print(ctypes.sizeof(D))

print(ctypes.sizeof(C))

print(ctypes.sizeof(D) - ctypes.sizeof(C))

# Test ctypes.CField in a union
class U(ctypes.Union):
    _fields_ = [("x", ctypes.c_int),
                ("y
