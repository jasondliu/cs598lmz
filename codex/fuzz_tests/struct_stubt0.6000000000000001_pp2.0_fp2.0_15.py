from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 4
s.format = 'i'

def _unpack(data):
    return s.unpack(data)[0]

def _pack(value):
    return s.pack(value)

def _is_big_endian():
    return s.pack('!i', 1)[0] == 1

def _is_little_endian():
    return s.pack('i', 1)[0] == 1

#
# Test
#

def test_unpack():
    assert _unpack(b'\x00\x00\x00\x00') == 0
    assert _unpack(b'\x00\x00\x00\x01') == 1
    assert _unpack(b'\x00\x00\x01\x00') == 256
    assert _unpack(b'\x00\x01\x00\x00') == 65536
    assert _unpack(b'\x01\x00\x00\x00') == 16777216
    assert _unpack(b
