import _struct
# Test _struct.Struct()
S = _struct.Struct('h')
S.size
S.format
S.pack(1)
S.pack(1, 2)
try:
    S.pack()
except TypeError:
    print('TypeError')
try:
    S.pack(1, 2, 3)
except TypeError:
    print('TypeError')
# Test _struct.Struct.unpack()
S = _struct.Struct('hh')
S.unpack(b'\x01\x00\x02\x00')
try:
    S.unpack(b'\x01\x00')
except _struct.error:
    print('_struct.error')
# Test _struct.Struct.unpack_from()
S = _struct.Struct('hh')
S.unpack_from(b'\x01\x00\x02\x00\x03\x00', 2)
S.unpack_from(b'\x01\x00\x02\x00\x03\x00', 0)
try:
    S.unpack_from
