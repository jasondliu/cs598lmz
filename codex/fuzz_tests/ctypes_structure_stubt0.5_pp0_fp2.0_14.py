import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
s.x = 1
s.y = 2

s1 = S(1, 2)
s2 = S(x=1, y=2)
s3 = S(y=2, x=1)
s4 = S(**dict(x=1, y=2))

assert s1.x == s2.x == s3.x == s4.x == 1
assert s1.y == s2.y == s3.y == s4.y == 2

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    def __init__(self, x, y):
        self.x = x
        self.y = y

s = S2(1, 2)
assert s.x == 1
assert s.y == 2
