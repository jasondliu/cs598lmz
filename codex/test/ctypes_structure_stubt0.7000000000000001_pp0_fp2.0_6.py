import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __init__(self, *args):
        super().__init__(*args)
        self.x = 42

c = S()
print(c.x)
