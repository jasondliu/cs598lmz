from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>2h'
s.size = s.calcsize(s.format)

def unpack(data):
    return s.unpack(data)

def pack(data):
    return s.pack(*data)

def unpack_from(data, offset=0):
    return s.unpack_from(data, offset)

