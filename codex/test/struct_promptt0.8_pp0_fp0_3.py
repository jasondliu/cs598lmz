import _struct
# Test _struct.Struct.format
struct_format = _struct.Struct('<5s5s').format
assert struct_format == '<5s5s'

# Test _struct.Struct.[un]pack
struct_pack = _struct.Struct('<5s5s').pack
struct_unpack = _struct.Struct('<5s5s').unpack
assert struct_pack(b'a', b'b') == b'a\x00\x00\x00\x00b\x00\x00\x00'
assert struct_unpack(b'a\x00\x00\x00\x00b\x00\x00\x00') == (b'a', b'b')

# Test _struct.Struct.[un]pack_from
struct_pack = _struct.Struct('<5s5s').pack_into
struct_unpack = _struct.Struct('<5s5s').unpack_from
