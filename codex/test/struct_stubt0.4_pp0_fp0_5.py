from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = 4
def unpack(data):
    return s.unpack(data)[0]
def pack(data):
    return s.pack(data)

def get_pack_unpack(size, endian='>'):
    s = Struct.__new__(Struct)
    s.format = endian + str(size) + 's'
    s.size = size
    def unpack(data):
        return s.unpack(data)[0]
    def pack(data):
        return s.pack(data)
    return pack, unpack

def get_pack_unpack_int(size, endian='>'):
    s = Struct.__new__(Struct)
    s.format = endian + str(size) + 's'
    s.size = size
    def unpack(data):
        return s.unpack(data)[0]
    def pack(data):
        return s.pack(data)
