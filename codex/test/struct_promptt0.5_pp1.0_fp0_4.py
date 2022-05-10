import _struct
# Test _struct.Struct
struct = _struct.Struct("i")
# Test _struct.calcsize
assert struct.size == 4
# Test _struct.pack
assert struct.pack(1) == b'\x01\x00\x00\x00'
# Test _struct.unpack
assert struct.unpack(b'\x01\x00\x00\x00') == (1,)
# Test _struct.iter_unpack
assert list(struct.iter_unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00')) == [(1,), (2,)]
# Test _struct.pack_into
buf = bytearray(8)
struct.pack_into(buf, 0, 1)
assert buf == b'\x01\x00\x00\x00\x00\x00\x00\x00'
# Test _struct.unpack_from
