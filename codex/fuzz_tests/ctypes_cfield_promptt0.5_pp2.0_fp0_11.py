import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.CField, 0),
    ]

p = POINT(1, 2, 3)
print(p.z)
print(p.x)
print(p.y)

p.z = 4
print(p.z)
print(p.x)
print(p.y)

p.x = 5
print(p.z)
print(p.x)
print(p.y)

# Test ctypes.CField with arrays
class POINT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.CField, (0, 1)),
    ]

p = POINT(1, 2, 3)
print(p.z)
print(p.x)
print(p.y)


