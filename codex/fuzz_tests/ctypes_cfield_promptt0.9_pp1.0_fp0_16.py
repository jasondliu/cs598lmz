import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [("f", ctypes.CField, 2)]
class C(ctypes.Union):
    _fields_ = [("s", S)]
c = C()
c.s.f = 3
print c.s.f
print c._objects_.keys()

libc = ctypes.CDLL(None)
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.CField, 2), ("y", ctypes.CField, 2)]
point = POINT()
point.x = 5
point.y = 6
res = libc.SetCursorPos(point)
print res

# Test ctypes.Array
class X(ctypes.Array):
    _type_ = ctypes.c_int16
    _length_ = 2
x = X()
x.value = (3, 4) # this forces x.value to be a python tuple...
print x.value
print "alignment of x:", x._align()

# Test ctypes.PyCFunc
