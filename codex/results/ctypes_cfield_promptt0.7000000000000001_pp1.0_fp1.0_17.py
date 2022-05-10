import ctypes
# Test ctypes.CField()
import sys
from ctypes import *
class X(Union):
    _fields_ = [("a", c_int),
                ("b", c_long),
                ("c", c_char_p),
                ("d", c_double)]

print X.a
print X.b
print X.c
print X.d

x = X()
print x.a
print x.b
print x.c
print x.d
x.a = 3
print x.a
print x.b
print x.c
print x.d
x.b = 4
print x.a
print x.b
print x.c
print x.d
x.c = "hello"
print x.a
print x.b
print x.c
print x.d
x.d = 1.0
print x.a
print x.b
print x.c
print x.d
print X.a._offset_
print X.b._offset_
print X.c._offset_
print X.d._offset_
