from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<l'
s.size = 4

def unpack(data):
    return s.unpack(data)

def pack(data):
    return s.pack(data)

def unpack_from(data, offset=0):
    return s.unpack_from(data, offset)

def pack_into(data, offset, value):
    s.pack_into(data, offset, value)
