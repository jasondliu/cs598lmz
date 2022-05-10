import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

    def __init__(self):
        self.x = 42

s = S()
print(s.x)
