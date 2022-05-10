import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(object):
    def __init__(self):
        self.s = S()
        self.s.x = 1

class B(object):
    def __init__(self):
        self.s = S()
        self.s.x = 2

class C(A, B):
    pass

c = C()
