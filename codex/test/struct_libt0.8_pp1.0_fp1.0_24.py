import _struct
import sys


def _is_valid_endianness(byteorder):
    return byteorder in ['@', '=', '<', '>', '!', '|']


def _is_native_endianness(byteorder):
    return byteorder == '@' or (byteorder == '=' and sys.byteorder == 'little')


_pack_intfmt = {
    1: 'b',
    2: 'h',
    4: 'l',
    8: 'q',
}

_unpack_byteorder = {
    '@': '@',
    '=': '@',
    '<': '@',
    '>': '!',
    '!': '!',
    '|': '|',
}

_unpack_intfmt = {
    1: 'b',
    2: 'h',
    4: 'l',
    8: 'q',
}

