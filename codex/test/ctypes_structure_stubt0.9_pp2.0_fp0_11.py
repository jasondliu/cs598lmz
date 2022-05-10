import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __init__(self):
        self.x = -1
    def func_0(self):
        self.x = 0
    def func_1(self):
        self.x = 1

