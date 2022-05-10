import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CFUNCTYPE(c_int, c_int, c_int)(func)(1, 2)

# Test ctypes.POINTER
POINTER(c_int)(c_int(42))

# Test ctypes.Structure
class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

Point(1, 2)

# Test ctypes.Union
class Coordinate(Union):
    _fields_ = [("x", c_int), ("y", c_int)]

Coordinate(x=1)

# Test ctypes.BigEndianStructure
class BigEndianPoint(BigEndianStructure):
    _fields_ = [("x", c_int), ("y", c_int)]

BigEndianPoint(1, 2)

# Test ctypes.LittleEndianStructure
class LittleEndianPoint(LittleEndianStructure):
    _fields_ = [("x", c_int), ("y", c_int
