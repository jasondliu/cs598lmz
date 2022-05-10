import ctypes
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    
p = Point(1, -1)
p.x

p._fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

p.a

# Test ctypes.BigEndianStructure
class BigEndPoint(ctypes.BigEndianStructure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    
t = BigEndPoint._string_at(ctypes.addressof(p))
t

# Test ctypes.LittleEndianStructure
class LittleEndPoint(ctypes.LittleEndianStructure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    
t = LittleEndPoint._string_at(ctypes.addressof(p))
t

# Test ctypes.Union
class UnionExample(ct
