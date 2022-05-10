import _struct
# Test _struct.Struct
assert _struct.Struct(b'hhl').size == 8
assert _struct.Struct(b'hhl').format == b'hhl'
assert _struct.Struct(b'hhl')(1, 2, 3) == b'\x01\x00\x02\x00\x00\x00\x00\x03'
assert _struct.Struct(b'hhl').unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03') == (1, 2, 3)
assert _struct.Struct(b'hhl').unpack_from(b'abcdef\x01\x00\x02\x00\x00\x00\x00\x03') == (1, 2, 3)
# Test _struct.error
try:
  _struct.Struct(b'hhi')
  raise Exception('_struct.error not raised')
except _struct.error:
  pass
# Test _struct.pack
assert _struct.pack(b'hhl', 1, 2, 3) == b
