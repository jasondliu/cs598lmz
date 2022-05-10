from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<l'
s.size = 4

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)

def pack_into(buffer, offset, data):
    return s.pack_into(buffer, offset, data)

def unpack_from(buffer, offset):
    return s.unpack_from(buffer, offset)[0]

def unpack_from_buffer(buffer, offset):
    return s.unpack_from(buffer, offset)[0]
