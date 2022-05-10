from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = calcsize(s.format)

ENDIANNESS = {
    b'\x49\x49\x2A': '<',
    b'\x4D\x4D\x00': '>',
    b'\x00\x00\x2A': '<',
    b'\x00\x00\x00': '>',
}


def unpack_from(data, offset=0):
    return Struct.unpack_from(s, data, offset)


def pack_into(data, offset, *args, **kwargs):
    if kwargs.get('bigendian', False):
        s.format = '>3s3sHH'
    return Struct.pack_into(s, data, offset, *args, **kwargs)


def unpack(data, offset=0, **kwargs):
    return unpack_from(data[offset:], offset)

