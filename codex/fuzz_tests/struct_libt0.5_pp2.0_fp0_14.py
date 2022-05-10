import _struct

from . import _utils
from ._utils import _decode_str, _encode_str, _check_size, _check_arg

def _make_struct(size, alignment):
    return _struct.Struct(str(size) + "s")


class _RawArray(object):
    """
    An array of raw bytes.

    This is an internal class used by the ctypes module.  It is not
    documented.

    """

    def __init__(self, typecode_or_type, size_or_initializer):
        if isinstance(typecode_or_type, str):
            self._type_ = _RawArrayType(typecode_or_type)
            self._size_ = size_or_initializer
            self._length_ = size_or_initializer
        else:
            self._type_ = typecode_or_type
            self._size_ = typecode_or_type._size_
            self._length_ = len(size_or_initializer)
            self._buffer = size_or_initializer

    def __re
