import ctypes
# Test ctypes.CField class
class Header(ctypes.BigEndianStructure):
    _pack_ = 1
    _fields_ = [("field1", ctypes.c_ubyte),
                ("field2", ctypes.c_ubyte),
                ("field3", ctypes.c_ubyte)]

print(Header._fields_)
print(Header._fields_[0])

print(ctypes.sizeof(Header._fields_[0]))
print(type(Header._fields_[0]))
print(Header._fields_[0])
print(len(Header._fields_[0]))

print(Header._fields_[0][0])
print(type(Header._fields_[0][0]))

print(Header._fields_[0][1])
print(type(Header._fields_[0][1]))
