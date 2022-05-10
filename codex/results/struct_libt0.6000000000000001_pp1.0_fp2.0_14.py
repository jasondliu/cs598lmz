import _struct
import array
import sys

# Python 2/3 compatibility
if sys.version_info[0] > 2:
    xrange = range

def _unpacker_factory(format, endianness):
    formats = {'@': 'native', '<': 'little', '>': 'big'}
    endian_format = formats[endianness]
    return struct.Struct('{}{}'.format(endian_format, format))

def _unpack(format, endianness, data):
    unpacker = _unpacker_factory(format, endianness)
    return unpacker.unpack(data)

def _unpack_from(format, endianness, buffer, offset=0):
    unpacker = _unpacker_factory(format, endianness)
    return unpacker.unpack_from(buffer, offset)

def _calcsize(format, endianness):
    unpacker = _unpacker_factory(format, endianness)
    return unpacker.size


