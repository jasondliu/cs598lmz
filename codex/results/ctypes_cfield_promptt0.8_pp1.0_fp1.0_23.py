import ctypes
# Test ctypes.CField
#
# The C version has been tested previously.

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int), ("b", c_int)]
    _anonymous_ = ("b",)

print X.a
print X().a

try:
    X.b
except AttributeError:
    print "X.b: ok"
else:
    raise Exception, "X.b: oops"

try:
    X().b
except AttributeError:
    print "X().b: ok"
else:
    raise Exception, "X().b: oops"

print X.a.__name__

try:
    X.a.__doc__
except AttributeError:
    print "X.a.__doc__: ok"

print X.a._type_
print X.a._offset_
assert isinstance(X.a._type_, TypeType)
assert isinstance(X.a._offset_, int)

try:
    X.b._type_
except Att
