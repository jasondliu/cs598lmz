import _struct

from . import _util


def _pack(format, *args):
    return _struct.pack(format, *args)


def _unpack(format, *args):
    return _struct.unpack(format, *args)


class _Struct(object):
    def __init__(self, *args, **kwargs):
        self.__struct = _struct.Struct(*args, **kwargs)

    def pack(self, *args):
        return self.__struct.pack(*args)

    def unpack(self, *args):
        return self.__struct.unpack(*args)


_uint8_t = _Struct('B')
_uint16_t = _Struct('H')
_uint32_t = _Struct('I')
_uint64_t = _Struct('Q')
_int8_t = _Struct('b')
_int16_t = _Struct('h')
_int32_t = _Struct('i')
_int64_t = _Struct('q')
_float_t = _Struct('f')
_
