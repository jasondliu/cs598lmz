import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_double()

    def __init__(self, isize, dsize):
        self.x = ctypes.c_int(isize)
        self.y = ctypes.c_double(dsize)    

class M(ctypes.Structure):
    s = S(4,8.0)
    z = ctypes.c_int()
    def __init__(self,z):
        self.z = ctypes.c_int(z)
