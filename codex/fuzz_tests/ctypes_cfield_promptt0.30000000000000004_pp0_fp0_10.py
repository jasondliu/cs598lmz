import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('c', C)]

d = D()
d.c.a = 1
d.c.b = 2

print d.c.a, d.c.b

# Test ctypes.CArray
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('c', C * 2)]

d = D()
d.c[0].a = 1
d.c[0].b = 2
d.c[1].a = 3
d.c[1].b = 4

print d.c[0].a, d.c[0].b
print d.c[1].a, d.c[1].b

# Test
