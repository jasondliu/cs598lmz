import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("d", ctypes.c_int), ("c", C)]

d = D()
d.c.a = 1
d.c.b = 2
print d.c.a
print d.c.b
# Test ctypes.CArray
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int * 4)]

c = C()
c.a[0] = 1
c.a[1] = 2
c.a[2] = 3
c.a[3] = 4
print c.a[0]
print c.a[1]
print c.a[2]
print c.a[3]
# Test ctypes.CArray
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char * 4)]


