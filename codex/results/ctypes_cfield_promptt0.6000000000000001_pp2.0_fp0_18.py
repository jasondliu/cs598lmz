import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
    ]
    def __repr__(self):
        return 'POINT({}, {}, {})'.format(self.x, self.y, self.z)

p = POINT(1, 2, 3)
print(ctypes.sizeof(p))
print(p)
# Test ctypes.CField and ctypes.CField.from_param
class POINT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
    ]
    def __repr__(self):
        return 'POINT({}, {}, {})'.format(self.x, self.y, self.z)

p = POINT(1, 2, 3)
print(ctypes.sizeof
