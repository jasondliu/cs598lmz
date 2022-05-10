import ctypes
# Test ctypes.CField
import collections

class C(ctypes.Structure):
    _fields_ = (("a", ctypes.c_uint),)

class D(ctypes.Structure):
    _fields_ = (("a", ctypes.c_uint),)

class E(ctypes.Structure):
    _fields_ = (("a", ctypes.c_uint),)


C.D = D
D.E = E

print(C)
# <class '__main__.C'>
print(C._fields_)
# [('a', <class 'ctypes.c_uint'>)])
print(C.D)
# <class '__main__.D'>
print(C.D._fields_)
# [('a', <class 'ctypes.c_uint'>)])
print(C.D.E)
# <class '__main__.E'>
print(C.D.E._fields_)
# [('a', <class 'ctypes.c_uint'>)])

# Test ctypes.CField
print(C.
