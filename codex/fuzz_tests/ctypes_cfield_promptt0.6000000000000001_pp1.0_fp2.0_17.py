import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_float), ('y', ctypes.c_float)]
    def __init__(self, x, y):
        super(POINT, self).__init__(x, y)

class SIZE(ctypes.Structure):
    _fields_ = [('width', ctypes.c_float), ('height', ctypes.c_float)]
    def __init__(self, width, height):
        super(SIZE, self).__init__(width, height)

class RECT(ctypes.Structure):
    _fields_ = [('origin', POINT), ('size', SIZE)]
    def __init__(self, origin, size):
        super(RECT, self).__init__(origin, size)

p = POINT(1, 2)
s = SIZE(3, 4)
r = RECT(p, s)
assert r.origin.x == 1 and r.origin.y == 2
assert r.size.width == 3 and r.
