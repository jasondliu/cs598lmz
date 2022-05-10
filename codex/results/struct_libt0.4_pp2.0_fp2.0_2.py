import _struct
from _struct import *

def struct_unpack(fmt, data):
    return _struct.unpack(fmt, data)

def struct_pack(fmt, *args):
    return _struct.pack(fmt, *args)

def struct_calcsize(fmt):
    return _struct.calcsize(fmt)

def struct_iter_unpack(fmt, data):
    size = _struct.calcsize(fmt)
    for i in xrange(0, len(data), size):
        yield _struct.unpack(fmt, data[i:i+size])

def struct_pack_into(fmt, buf, offset, *args):
    return _struct.pack_into(fmt, buf, offset, *args)

def struct_unpack_from(fmt, buf, offset=0):
    return _struct.unpack_from(fmt, buf, offset)

def struct_iter_unpack_from(fmt, buf, offset=0):
    size = _struct.cal
