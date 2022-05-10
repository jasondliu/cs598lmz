from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")

def pack(x):
    return s.pack(x)

def unpack(x):
    return s.unpack(x)[0]

def pack_into(buf, offset, x):
    s.pack_into(buf, offset, x)

def unpack_from(buf, offset):
    return s.unpack_from(buf, offset)[0]

def calcsize():
    return s.size

def test():
    import sys
    import struct
