import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('x', ctypes.c_int),
                ('a', ctypes.c_int)]

    def __init__(self):
        self.y = 10
        self.z = 20
        self.a = 30

x = S()
