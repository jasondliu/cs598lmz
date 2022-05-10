import _struct

from . import _common


def _parse_struct(fmt, buf):
    return _struct.unpack(fmt, buf)


def _parse_struct_from(fmt, buf, offset):
    return _struct.unpack_from(fmt, buf, offset)


def _parse_bytes(length, buf):
    return buf[:length], buf[length:]


def _parse_bytes_from(length, buf, offset):
    return buf[offset:offset + length], buf[offset + length:]


def _parse_int(buf):
    return int.from_bytes(buf, 'little'), buf[4:]


def _parse_int_from(buf, offset):
    return int.from_bytes(buf[offset:offset + 4], 'little'), buf[offset + 4:]


def _parse_string(buf):
    length, buf = _parse_int(buf)
    string, buf = _parse_bytes(length, buf)
