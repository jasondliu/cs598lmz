import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    def __getattr__(self, name):
        return name

s = S()
