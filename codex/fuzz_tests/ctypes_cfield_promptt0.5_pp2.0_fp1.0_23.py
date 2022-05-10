import ctypes
# Test ctypes.CField
#

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int), ("b", c_int), ("c", c_int)]
    _anonymous_ = ("b",)

x = X()

print x.a
print x.b
print x.c

x.a = 1
x.b = 2
x.c = 3

print x.a
print x.b
print x.c

print x.a == x.b
print x.a == x.c

print x.a == 1
print x.b == 2
print x.c == 3

print x.a == 2
print x.b == 1
print x.c == 1

print x.a == 3
print x.b == 3
print x.c == 1

print x.a == 3
print x.b == 3
print x.c == 2

print x.a == 3
print x.b == 3
print x.c == 3

print x.a == 2
print x.b ==
