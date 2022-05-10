import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(object):
    def __init__(self):
        self.s = S()
        self.s.x = 1

a = A()
a.s.x = 2
print a.s.x
</code>

