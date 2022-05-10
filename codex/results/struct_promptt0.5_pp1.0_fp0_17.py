import _struct
# Test _struct.Struct
struct = _struct.Struct('i')
assert struct.size == 4
# Test _struct.pack
assert struct.pack(42) == b'*\x00\x00\x00'
# Test _struct.unpack
assert struct.unpack(b'*\x00\x00\x00') == (42,)
# Test _struct.unpack_from
assert struct.unpack_from(b'*\x00\x00\x00', 0) == (42,)
# Test _struct.calcsize
assert struct.calcsize('i') == 4
# Test _struct.error
try:
    struct.pack('i', 'a')
except _struct.error:
    pass
else:
    raise Exception("should have raised _struct.error")
# Test _struct.pack_into
buf = bytearray(b'\x00' * 8)
struct.pack_into(buf, 0, 42)
assert buf == b'*\x00\x00\x00\x00\x00\x00\x00'
