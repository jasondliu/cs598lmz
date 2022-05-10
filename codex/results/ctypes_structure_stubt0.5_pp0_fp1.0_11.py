import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3

s = S()
print(s.x)
print(s.y)
print(s.z)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)
               ]
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3

s2 = S2()
print(s2.x)
print(s2.y)
print(s2.z)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)

