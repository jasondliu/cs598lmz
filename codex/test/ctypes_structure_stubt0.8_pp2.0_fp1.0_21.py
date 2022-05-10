import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_long
    def __init__(self):
        self.x = 7.0
        self.y = 3

a = S()
