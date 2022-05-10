import _struct

def unpack_from(fmt, buf, offset=0):
    return _struct.unpack_from(fmt, buf, offset)

def unpack_from_endian(fmt, buf, offset=0, endian="<"):
    return _struct.unpack_from(endian + fmt, buf, offset)

def unpack_from_be(fmt, buf, offset=0):
    return _struct.unpack_from(">" + fmt, buf, offset)

def unpack_from_le(fmt, buf, offset=0):
    return _struct.unpack_from("<" + fmt, buf, offset)

def pack_into(fmt, buf, offset, *args):
    return _struct.pack_into(fmt, buf, offset, *args)

def pack_into_endian(fmt, buf, offset, endian="<", *args):
    return _struct.pack_into(endian + fmt, buf, offset, *args)

