import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
print s.x, s.y
s.x = 1
s.y = 2
print s.x, s.y

print s.__dict__

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    def __init__(self):
        self.x = 1
        self.y = 2

s = S()
print s.x, s.y

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    def __init__(self, x, y):
        self.x = x
        self.y = y

s = S(1, 2)
print s.x, s.y

class S(ctypes.
