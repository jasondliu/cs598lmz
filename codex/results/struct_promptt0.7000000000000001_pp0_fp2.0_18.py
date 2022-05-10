import _struct
# Test _struct.Struct
for code in 'xcbhilfdsp':
    s = _struct.Struct('<' + code)
    packed = s.pack(42)
    unpacked = s.unpack(packed)
    assert unpacked == (42,)
    assert s.size == _struct.calcsize('<' + code)

# See if array works correctly
import array
a = array.array('i', [0, 1, 2, 3, 4])
packed = _struct.pack('P' + 'i' * len(a), a)
unpacked = _struct.unpack('P' + str(len(a)) + 'i', packed)
assert unpacked == tuple(a)

# See if bytes_ works correctly
import binascii, sys
a = b'\x01\x02\x03\x04\x05\x06\x07\x08'
packed = _struct.pack('Pc', a)
unpacked = _struct.unpack('Pc', packed)
assert unpacked == (a,)

# See if bytearray works correctly
