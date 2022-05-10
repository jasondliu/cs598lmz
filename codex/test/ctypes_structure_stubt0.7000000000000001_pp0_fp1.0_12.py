import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        
s = S()

s.x = 1
