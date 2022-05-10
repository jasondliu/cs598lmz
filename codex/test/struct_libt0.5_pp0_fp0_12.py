import _struct

from .. import _util
from .. import _constants
from .. import _errors
from .. import _compat
from .. import _stream


def _read_struct(stream, fmt):
    size = _struct.calcsize(fmt)
    data = stream.read(size)
    if len(data) != size:
        raise _errors.UnexpectedEndOfStreamError()
    return _struct.unpack(fmt, data)


def _read_struct_le(stream, fmt):
    return _read_struct(stream, "<" + fmt)


def _read_struct_be(stream, fmt):
    return _read_struct(stream, ">" + fmt)


def _read_struct_array(stream, fmt, count):
    size = _struct.calcsize(fmt)
    data = stream.read(size * count)
    if len(data) != size * count:
        raise _errors.UnexpectedEndOfStreamError()
    return _struct.unpack(fmt * count, data)


