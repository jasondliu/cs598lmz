import ctypes
# Test ctypes.CField.from_address method

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint8), ("y", ctypes.c_uint8)]

a = Point()

# Note that one of the fields is negative (x == -1), so accessing
# the structure fields through this pointer should raise an exception
p = ctypes.cast(id(a) + 3, ctypes.POINTER(Point))

try:
    p.contents.x
except TypeError:
    pass
else:
    print "expected an exception"

# But this one should work
cf = ctypes.CField.from_address(id(a), p._type_, "x")
result = cf.get()
if result == 255:
    print "ok"
else:
    print "wrong value"
