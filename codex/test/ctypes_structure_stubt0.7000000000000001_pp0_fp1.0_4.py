import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double

class A(object):
    def __init__(self):
        self.s = S()
        self.s.x = 3

a = A()

