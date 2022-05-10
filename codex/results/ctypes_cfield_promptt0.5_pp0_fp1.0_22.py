import ctypes
# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.CField),
    ]

print X.b
print X.b.offset
print X.b.size

print ctypes.c_int.offset
print ctypes.c_int.size

try:
    ctypes.c_int.offset = 10
except AttributeError:
    print "cannot set offset"
else:
    print "set offset"

try:
    ctypes.c_int.size = 10
except AttributeError:
    print "cannot set size"
else:
    print "set size"
