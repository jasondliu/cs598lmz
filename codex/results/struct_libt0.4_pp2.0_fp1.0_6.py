import _struct

from . import _compat


def _read_struct(fileobj, format):
    size = struct.calcsize(format)
    data = fileobj.read(size)
    if len(data) != size:
        raise ValueError("Unexpected end of file")
    return _struct.unpack(format, data)


def _read_struct_le(fileobj, format):
    size = struct.calcsize(format)
    data = fileobj.read(size)
    if len(data) != size:
        raise ValueError("Unexpected end of file")
    return _struct.unpack_from(format, data, 0)


def _read_struct_be(fileobj, format):
    size = struct.calcsize(format)
    data = fileobj.read(size)
    if len(data) != size:
        raise ValueError("Unexpected end of file")
    return _struct.unpack_from(format, data, 0, _struct.STRUCT_BE)


def _read_uint8(fileobj):
    return
