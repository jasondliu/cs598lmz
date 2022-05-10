import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(ctypes.Structure):
    _fields_ = [("s", S)]

c = C()
c.s.x = 42
print(c.s.x)
</code>

