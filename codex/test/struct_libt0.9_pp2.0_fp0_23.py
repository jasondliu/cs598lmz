import _struct
struct_unpack = _struct.unpack

from collections import namedtuple

class InvalidMZHeader(Exception):
    pass

PE_TYPE = ['PE32', 'PE32+', 'ROM']

class OptionalHeader(object):
    fmt = '=HHIHHHHHIHHIIQQQ'
    fmt_size = struct_calcsize(fmt)
