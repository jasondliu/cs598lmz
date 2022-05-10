import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class C(ctypes.Structure):
    _fields_ = [('s', S)]

c = C()
c.s.x = 1
c.s.y = 2
c.s.z = 3
print(c.s.x, c.s.y, c.s.z)
</code>

