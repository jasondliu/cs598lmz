import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class D(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class C(ctypes.Structure):
    _fields_ = [("s", S), ("d", D)]

c = C()
c.s.x = 1
c.s.y = 2
c.s.z = 3
c.d.x = 4
c.d.y = 5
c.d.z = 6

print c.s.x
print c.s.y
print c.s.z
print c.d.x
print c.d.y
print c.d.z
