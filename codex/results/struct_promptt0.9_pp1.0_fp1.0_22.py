import _struct
# Test _struct.Struct().pack_into() with sizes and endian'ness.

buffer = bytearray(13)
b = buffer[3:-3]

a = _struct.Struct('<f').pack_into(b, 3, 3.14)
assert a is None and b[:] == b'\00\00\x18\x93@\00\00'

a = _struct.Struct('>f').pack_into(b, 0, 3.14)
assert a is None and b[:] == b'\x93\x18\x00\x00\x00\x00@\00'

a = _struct.Struct('<i').pack_into(b, 4, 42)
assert a is None and b[:] == b'@\x18\x00\x00*\x00\x00\x00'

a = _struct.Struct('<q').pack_into(b, 3, 0x9876543210)
asser
