import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
class A(ctypes.Array):
    _type_ = S
    _length_ = 2

a = A()
print a[0].x, a[1].x
a[0].x, a[1].x = 1, 2
for i in a:
    print i.x

print "==== " * 8

class A(ctypes.PyCSimpleType):
    _type_ = "p"
    _subtype_ = "h"

class X(ctypes.PyCSimpleType):
    _type_ = "P"
    _subtype_ = A

a = A(1)
print a
ptr = ctypes.pointer(a)
print repr(ptr)
