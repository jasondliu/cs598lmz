import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C.b))]

c = C(1, 2)
d = D(3, c)
print d.a, d.b

d.b = 4
print d.a, d.b
print c.a, c.b

d.a = 5
print d.a, d.b
print c.a, c.b

try:
    d.b = "hello"
except TypeError:
    print "TypeError"

# Test ctypes.CField with a pointer

class P(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Q(ctypes.Structure):
    _fields_ =
