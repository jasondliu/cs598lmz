from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2i'
s.size = 8

def unpack(data):
    return s.unpack(data)

def pack(data):
    return s.pack(*data)

def unpack_from(data, offset):
    return s.unpack_from(data, offset)

def pack_into(data, offset, values):
    return s.pack_into(data, offset, *values)

def calcsize():
    return s.size

def pack_into_and_advance(data, offset, values):
    pack_into(data, offset, values)
    return offset + calcsize()

def unpack_from_and_advance(data, offset):
    return unpack_from(data, offset), offset + calcsize()

def unpack_from_and_advance_with_default(data, offset, default):
    if offset + calcsize() > len(data):
        return default, offset + calcsize()
    return unpack_from(data, offset), offset + cal
