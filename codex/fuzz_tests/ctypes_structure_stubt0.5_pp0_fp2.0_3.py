import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
print(s.x)
print(s.y)
print(s.x + s.y)
s.x = 1
s.y = 2
print(s.x)
print(s.y)
print(s.x + s.y)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    def __init__(self, x, y):
        self.x = x
        self.y = y

s2 = S2(3, 4)
print(s2.x)
print(s2.y)
print(s2.x + s2.y)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_
