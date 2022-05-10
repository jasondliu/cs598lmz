import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(100)

    def __init__(self):
        super(S, self).__init__(x = 1)


s = S()
