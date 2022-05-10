import ctypes
# Test ctypes.CField.__get__

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C)]

class E(object):
    _fields_ = [("c", C),
                ("d", D)]

    def __init__(self):
        self.c = C()
        self.d = D()

e = E()
e.c.a = 1
e.d.c.b = 2

print e.c.a
print e.d.c.a
print e.d.c.b
