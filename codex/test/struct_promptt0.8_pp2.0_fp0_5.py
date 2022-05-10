import _struct
# Test _struct.Struct
s = _struct.Struct('llh')
print(s.size, s.pack(1, 2, 3))
# Test _struct.calcsize
print(_struct.calcsize('llh'))
# Test _struct.pack
print(_struct.pack('llh', 1, 2, 3))
# Test _struct.unpack
print(_struct.unpack('lllh', b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00'))
# Test _struct.unpack_from
print(_struct.unpack_from('llh', b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00', 12))

import _traceback
# Test _trace
