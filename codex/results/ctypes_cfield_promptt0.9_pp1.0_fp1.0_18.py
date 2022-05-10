import ctypes
# Test ctypes.CField
class MyCF(ctypes._CField):
    _type_ = "i"
    _length_ = 2
    _offset_ = 0
MyCF._index_ = 0

# Test ctypes.CDataTypeMeta
class MyCM(ctypes.CDataTypeMeta):
    _fields_ = [MyCF]

# Test ctypes.CDatatype
class MyCD(int, metaclass=MyCM):
    _pack_ = 1
    _ctype_ = MyCF
MyCD._index_ = 0
MyCD._length_ = 2

# Test ctypes.Union
class MyUn(ctypes.Union):
    _fields_ = [('a', MyCD)]

# Test ctypes.Struct
class MySt(ctypes.Struct):
    _fields_ = [MyCF]

# Test ctypes.Array
class MyAr(ctypes.Array):
    _type_ = MyCD
    _length_ = 2
