import _struct
# Test _struct.Struct

# Test the basic methods

s = _struct.Struct('i')

assert s.size == 4
assert s.format == 'i'

assert s.pack(1) == b'\x01\x00\x00\x00'
assert s.pack(1, 2) == b'\x01\x00\x00\x00'
assert s.pack_into(bytearray(b'0123'), 0, 1) == None
assert s.unpack(b'\x01\x00\x00\x00') == (1,)
assert s.unpack_from(b'0123', 0) == (1,)

# Test the format string

assert _struct.Struct('xcbhilfdspP?').format == 'xcbhilfdspP?'

try:
    _struct.Struct('abc')
except ValueError:
    pass
else:
    print('ValueError expected')

try:
    _struct.Struct('cabc')
except ValueError:
    pass
else:
    print('ValueError expected')
