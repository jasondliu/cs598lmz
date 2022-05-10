import _struct
import struct
import xdrlib

_pad = _struct.Struct('x')
_int1 = _struct.Struct('!b')
_uint1 = _struct.Struct('!B')
_int2 = _struct.Struct('!h')
_uint2 = _struct.Struct('!H')
_int4 = _struct.Struct('!i')
_uint4 = _struct.Struct('!I')
_int8 = _struct.Struct('!q')
_uint8 = _struct.Struct('!Q')
_float4 = _struct.Struct('!f')
_float8 = _struct.Struct('!d')
_bool = _struct.Struct('!?')

class Packer(object):
    """
    Pack values into binary format.

    Initialize a Packer with a write function that takes a byte
    string to add to the packed stream.

    After initialization, call pack_*() methods to pack values,
    then call get_buffer() to retrieve the packed data.

    After the packed data has been retrieved, more values can be
    packed, and get
