from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>hhl'
s.size = s.calcsize(s.format)

def pack(data):
    return s.pack(*data)

def unpack(data):
    return s.unpack(data)

def unpack_from(data, offset=0):
    return s.unpack_from(data, offset)

def calcsize():
    return s.size
