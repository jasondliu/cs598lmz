import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(object):
    def __init__(self):
        self.x = S()

a = A()

a.x.x = 5

print a.x.x
</code>

