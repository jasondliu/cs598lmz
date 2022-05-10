import _struct
# Test _struct.Struct
assert _struct.Struct('hhl').size == 8
assert _struct.Struct('hhl').format == 'hhl'
assert _struct.Struct('hhl').unpack(b'\0\0\0\0\0\0\0\0') == (0, 0, 0)
assert _struct.Struct('hhl').unpack_from(b'\0\0\0\0\0\0\0\0') == (0, 0, 0)
assert _struct.Struct('hhl').pack(0, 0, 0) == b'\0\0\0\0\0\0\0\0'
assert _struct.Struct('hhl').pack_into(bytearray(8), 0, 0, 0, 0) == None
assert _struct.Struct('hhl').pack_into(bytearray(8), 0, 0, 0, 0) == None
# Test _struct.error
try:
    _struct.Struct('x')
except _struct.error as e:
    assert str(e) == 'bad char in struct format'
#
