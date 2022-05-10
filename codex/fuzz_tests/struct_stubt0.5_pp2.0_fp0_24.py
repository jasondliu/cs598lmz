from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.format = Struct.format
s.pack = Struct.pack
s.unpack = Struct.unpack
s.unpack_from = Struct.unpack_from

def pack(fmt, *args):
    return s.pack(fmt, *args)

def unpack(fmt, *args):
    return s.unpack(fmt, *args)

def unpack_from(fmt, *args):
    return s.unpack_from(fmt, *args)

def calcsize(fmt):
    return s.size

def pack_into(fmt, buf, offset, *args):
    s.pack_into(buf, offset, fmt, *args)

def unpack_from(fmt, buf, offset=0):
    return s.unpack_from(fmt, buf, offset)

# Make it so that booleans are unpacked as integers, not as booleans.
def unpack(fmt, *args):
    result = s.unpack(f
