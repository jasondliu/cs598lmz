import ctypes
# Test ctypes.CFields are constructable
class C(ctypes.LittleEndianStructure):
    _fields_ = [("b", ctypes.c_ubyte, 4),
                ("c", ctypes.c_ubyte, 2),
                ("a", ctypes.c_ubyte, 2)]

C(1)
C(a=1)
C(b=1)
C(c=1)
C(a=1, c=2)
C(0, b=2)
try:
    C(1, 2, 3)
except TypeError:
    pass
try:
    C(1, 2)
except TypeError:
    pass
try:
    C(1, b=2, c=3)
except TypeError:
    pass
try:
    C(a=1, b=2, c=3)
except TypeError:
    pass

D = ctypes.LittleEndianStructure
D.__doc__ = "Test.__doc__"
D._fields_ = []
E = ctypes.BigEndianStructure
E.
