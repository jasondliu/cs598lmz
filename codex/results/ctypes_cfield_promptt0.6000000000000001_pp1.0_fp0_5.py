import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class D(C):
    def __init__(self, value=0):
        super(D, self).__init__()
        self.x = value

c = C()
c.x = 42
print c.x

d = D(43)
print d.x

class E(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class F(E):
    def __init__(self, value=0):
        super(F, self).__init__()
        self.x = value

f = F(42)
print f.x
print f.y

# Test ctypes.CArray

class CA1(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int * 4)]

class CA2(CA1):
    def __init__(self, value=0):
