from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I"
s.size = 4
s.pack_into = lambda buffer, offset, value: buffer[offset:offset+4].from_bytes(value.to_bytes(4, byteorder="big"), byteorder="big")
s.unpack_from = lambda buffer, offset: int.from_bytes(buffer[offset:offset+4], byteorder="big")
s.unpack = lambda buffer: s.unpack_from(buffer, 0)

def pack_into(fmt, buffer, offset, *args):
    if isinstance(fmt, Struct):
        fmt.pack_into(buffer, offset, *args)
    else:
        struct.pack_into(fmt, buffer, offset, *args)

def unpack_from(fmt, buffer, offset=0):
    if isinstance(fmt, Struct):
        return fmt.unpack_from(buffer, offset)
    else:
        return struct.unpack_from(fmt, buffer, offset)

