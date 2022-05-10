import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("y", ctypes.CField)]

class Z(ctypes.Structure):
    _fields_ = [("z", ctypes.CField)]

class XYZ(ctypes.Union):
    _fields_ = [("xyz", Y),
                ("xyz", Z)]

print XYZ.xyz.offset
print XYZ.xyz.size
print XYZ.xyz.ctype
print XYZ.xyz.type
print XYZ.xyz.name
print XYZ.xyz.shape
print XYZ.xyz.dimensions
print XYZ.xyz.strides
print XYZ.xyz.format
print XYZ.xyz.readonly
print XYZ.xyz.raw
print XYZ.xyz.data
print XYZ.xyz.flags
print XYZ.xyz.itemsize
print XYZ.xyz.ndim
