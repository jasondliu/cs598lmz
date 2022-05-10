import _struct

from . import _common

def _get_struct(format):
    return _struct.Struct(format)

def _get_unpacker(format):
    return _struct.Struct(format).unpack

def _get_packer(format):
    return _struct.Struct(format).pack

def _get_unpack_from(format):
    return _struct.Struct(format).unpack_from

def _get_pack_into(format):
    return _struct.Struct(format).pack_into

def _get_size(format):
    return _struct.Struct(format).size

def _get_unpack_from_iter(format):
    unpack = _struct.Struct(format).unpack_from
    def unpack_from_iter(buffer, offset=0):
        while True:
            yield unpack(buffer, offset)
            offset += _struct.Struct(format).size
    return unpack_from_iter

def _get_pack_into_iter(format):
    pack = _struct.Struct(format).pack
