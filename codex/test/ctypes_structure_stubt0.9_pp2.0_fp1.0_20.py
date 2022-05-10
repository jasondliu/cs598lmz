import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

    def __repr__(self):
        return '(%s, %s)'%(self.x, self.y)

