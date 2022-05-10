import ctypes
# Test ctypes.CField
# This tests that the ctypes.CField object, which is
# used internally by the ctypes type machinery, is
# accessible from Python.
# It should be possible that the CField object is used to
# implement a readonly attribute.
class Tag(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = ["a"]

class Tag2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

t = Tag()
t.a = 2
t.b = 3
print t.a, t.b
print t._fields_[0], Tag._fields_[0]
print t._anonymous_[0], Tag._anonymous_[0]
try:
    print Tag2._anonymous_[0]
except:
    print "Could not access _anonymous_ of Tag2"
Tag._fields_[0].__set__(t, 4)
print t.a
