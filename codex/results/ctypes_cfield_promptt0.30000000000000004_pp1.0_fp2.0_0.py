import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField(C, "a"))]

d = D()
d.a = 1
d.b = 2
d.c = 3
print d.a, d.b, d.c

d.c = 4
print d.a, d.b, d.c

d.a = 5
print d.a, d.b, d.c

try:
    d.c = "spam"
except TypeError:
    print "TypeError"

try:
    d.c = None
except TypeError:
    print "TypeError"

try:
    d.c = D()
except TypeError:
    print "TypeError"

try:
    d.c
