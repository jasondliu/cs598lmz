import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self):
        self.x = 1

c = C()

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

d = D()
d.x = c.x
print(d.x)
print(c.x)
c.x = 2
print(d.x)
print(c.x)
