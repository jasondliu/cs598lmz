import _struct
# Test _struct.Struct()

# Issue #4006: _struct.Struct() has a length argument, but it is ignored.
# This is a bug.

import _struct
import struct

def pack(fmt, *args):
    return struct.pack(fmt, *args)

def unpack(fmt, data):
    return struct.unpack(fmt, data)

def pack_into(fmt, buf, offset, *args):
    return struct.pack_into(fmt, buf, offset, *args)

def unpack_from(fmt, buf, offset=0):
    return struct.unpack_from(fmt, buf, offset)

def test_packed_size():
    assert _struct.calcsize('h') == 2
    assert _struct.calcsize('hh') == 4
    assert _struct.Struct('h').size == 2
    assert _struct.Struct('hh').size == 4

def test_pack():
    assert pack('hh', 1, 2) == b'\x01\x00\x02\x00'
   
