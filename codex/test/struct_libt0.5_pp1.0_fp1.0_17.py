import _struct

from . import _constants


def _convert_to_bytes(string):
    if isinstance(string, bytes):
        return string
    else:
        return string.encode()


def _convert_from_bytes(string):
    if isinstance(string, str):
        return string
    else:
        return string.decode()


def _get_struct_size(struct_format):
    return _struct.calcsize(struct_format)


# Structs

_struct_size_uint8 = _get_struct_size(">B")
_struct_size_uint16 = _get_struct_size(">H")
_struct_size_uint32 = _get_struct_size(">I")
_struct_size_uint64 = _get_struct_size(">Q")
