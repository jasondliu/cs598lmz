import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.CField)]

d = D()
d.a = 1
d.b = 2
d.c.x = 3
d.c.y = 4
print d.a, d.b, d.c.x, d.c.y

d2 = D.from_address(ctypes.addressof(d) + ctypes.sizeof(ctypes.c_int))
print d2.a, d2.b, d2.c.x, d2.c.y
print d2.c.__class__ is C

# Test ctypes.CFUNCTYPE

def func(x, y):
    return x + y

func_type = ctypes
