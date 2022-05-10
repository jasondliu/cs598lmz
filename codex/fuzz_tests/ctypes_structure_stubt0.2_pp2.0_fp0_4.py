import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(object):
    def __init__(self):
        self.s = S()
        self.s.x = 42

c = C()
print c.s.x
</code>

