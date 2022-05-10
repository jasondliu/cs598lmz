import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(object):
    def __init__(self):
        self.s = S()
        self.s.x = 1

c = C()
print c.s.x
c.s.x = 2
print c.s.x
</code>

