import ctypes
# Test ctypes.CField
#
# get it right
class A(ctypes.Structure):
    _fields_ = [("hi", ctypes.c_int)]
a = A()
a.hi = 10
print(a.hi)
assert a.hi == 10
#
# get it wrong
class X(ctypes.Structure):
    _fields_ = [("hi", ctypes.CField)]
x = X()
x.hi = 10
print(x.hi)
assert x.hi == 10
