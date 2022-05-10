import _struct

def pack(format, *args):
    return _struct.pack(format, *args)

def unpack(format, *args):
    return _struct.unpack(format, *args)

def unpack_from(format, *args):
    return _struct.unpack_from(format, *args)

def calcsize(format):
    return _struct.calcsize(format)

def pack_into(format, buffer, offset, *args):
    return _struct.pack_into(format, buffer, offset, *args)

def unpack_from(format, buffer, offset=0):
    return _struct.unpack_from(format, buffer, offset)

byte_order = _struct.byte_order
format_size = _struct.format_size
Struct = _struct.Struct

SIZE_OF_BYTE = calcsize('b')
SIZE_OF_UBYTE = calcsize('B')
SIZE_OF_SHORT = calcsize('h')
