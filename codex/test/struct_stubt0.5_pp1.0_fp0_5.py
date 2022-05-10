from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.format = Struct.format
s.pack = Struct.pack
s.unpack = Struct.unpack
s.pack_into = Struct.pack_into
s.unpack_from = Struct.unpack_from

_pack_ = s.pack
_unpack_ = s.unpack
_pack_into_ = s.pack_into
_unpack_from_ = s.unpack_from

def pack(fmt, *args):
    return _pack_(fmt, *args)

def unpack(fmt, string):
    return _unpack_(fmt, string)

def pack_into(fmt, buffer, offset, *args):
    return _pack_into_(fmt, buffer, offset, *args)

def unpack_from(fmt, buffer, offset=0):
    return _unpack_from_(fmt, buffer, offset)

error = Struct.error

