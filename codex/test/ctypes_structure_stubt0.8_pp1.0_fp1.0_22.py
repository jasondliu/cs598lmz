import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __init__(self, x=10):
        super(S, self).__init__(x=x)

s = S()
s.x = 20
