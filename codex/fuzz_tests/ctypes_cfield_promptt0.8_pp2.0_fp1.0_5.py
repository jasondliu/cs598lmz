import ctypes
# Test ctypes.CField.
class Struct(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int, 5),
        ('b', ctypes.c_int, 3),
        ('c', ctypes.c_int, 8),
    ]
    s = ctypes.CField(a, b)

print Struct.s.offset
print Struct.s.bitsize
# END TEST

class CField(object):
    __slots__ = "offset", "bitsize", "name", "type"
    def __init__(self, offset, bitsize, name, type):
        self.offset = offset
        self.bitsize = bitsize
        self.name = name
        self.type = type

    def __repr__(self):
        return '%s/%d' % (self.name, self.bitsize)
    def __str__(self):
        return self.__repr__()

class CFields(UserList):
    __slots__ = "type", "bitsize", "offset"
    def __init__
