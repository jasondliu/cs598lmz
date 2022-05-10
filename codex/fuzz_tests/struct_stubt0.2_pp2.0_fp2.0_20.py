from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>i'
s.size = 4

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)

def unpack_from(data, offset=0):
    return s.unpack_from(data, offset)[0]

def pack_into(data, offset, value):
    s.pack_into(data, offset, value)

def unpack_from_file(file):
    return s.unpack_from(file.read(4))[0]

def pack_into_file(file, value):
    s.pack_into(file, value)

def unpack_from_string(data, offset=0):
    return s.unpack_from(data, offset)[0]

def pack_into_string(data, offset, value):
    s.pack_into(data, offset, value)

def unpack_from_buffer(data, offset=0):
    return s.unpack_from(data, offset)[
