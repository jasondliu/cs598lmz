import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = [("anonymous", ctypes.c_int)]
    _pack_ = 1
    def __repr__(self):
        return ctypes.Structure.__repr__(self)
print X.a
print ctypes.Union.__bases__
print X.anonymous
print X.b
print X(a=1, b=2)
print X(a=1, anonymous=2)
print X(anonymous=1, b=2)
# Test ctypes.BigEndianStructure
class X(ctypes.BigEndianStructure):
    _fields_ = [("a", ctypes.c_byte), ("b", ctypes.c_byte)]
print X.a
print X.b
print X(a=1, b=2)
print X(b=1, a=2)
# Test ctypes.LittleEndianStructure
class X(ctypes.
