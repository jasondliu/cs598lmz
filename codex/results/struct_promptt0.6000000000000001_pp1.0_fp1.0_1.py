import _struct
# Test _struct.Struct.__repr__
_struct.Struct('i')
# Test _struct.Struct.pack
_struct.Struct('i').pack(1)
# Test _struct.Struct.unpack
_struct.Struct('i').unpack(b'\x00\x00\x00\x01')
# Test _struct.Struct.iter_unpack
list(_struct.Struct('i').iter_unpack(b'\x00\x00\x00\x01'))
# Test _struct.Struct.size
_struct.Struct('i').size
# Test _struct.Struct.format
_struct.Struct('i').format
# Test _struct.Struct.pack_into
b = bytearray(4)
_struct.Struct('i').pack_into(b, 0, 1)
# Test _struct.Struct.unpack_from
_struct.Struct('i').unpack_from(b'\x00\x00\x00\x01', 0)
# Test _struct.Struct.iter_unpack_from
list(_struct.Struct('i').iter_unpack
