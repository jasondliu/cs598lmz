from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = 4

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)

def unpack_from(data, offset=0):
    return s.unpack_from(data, offset)[0]

def pack_into(data, offset, value):
    return s.pack_into(data, offset, value)

def unpack_from_file(f):
    return unpack(f.read(4))

def pack_into_file(f, value):
    return f.write(pack(value))

def unpack_from_string(data, offset=0):
    return unpack_from(data, offset)

def pack_into_string(data, offset, value):
    return pack_into(data, offset, value)

def unpack_from_buffer(data, offset=0):
    return unpack_from(data, offset)

def pack_into_buffer(data, offset, value
