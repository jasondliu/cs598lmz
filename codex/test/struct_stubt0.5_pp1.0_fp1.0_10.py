from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = 8

def unpack(s, data):
    return s.unpack(data)

def pack(s, *data):
    return s.pack(*data)

def calcsize(s):
    return s.size

def pack_into(s, buffer, offset, *data):
    return s.pack_into(buffer, offset, *data)

def unpack_from(s, buffer, offset=0):
    return s.unpack_from(buffer, offset)

# def pack_into(s, buffer, offset, *data):
#     return s.pack_into(buffer, offset, *data)
