import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    def __str__(self):
        return 'x: %d, y: %d, z: %d' % (self.x, self.y, self.z)

class A(ctypes.Structure):
    _fields_ = [('s', S), ('i', ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [('s', S), ('i', ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('s', S), ('i', ctypes.c_int)]

class D(ctypes.Union):
    _fields_ = [('a', A), ('b', B), ('c', C)]

print D.a.s
print D.b.s
print D.c.s

d = D()
d.a.s.x = 10
d.a.s.y = 20
d.a.s.z
