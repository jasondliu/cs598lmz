import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    def __repr__(self):
        return "S(%s)" % self.x

s = S()
