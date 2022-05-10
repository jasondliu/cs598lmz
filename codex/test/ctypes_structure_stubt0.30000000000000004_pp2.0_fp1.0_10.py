import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

s = S(1, 2, 3)
print(s.x, s.y, s.z)
