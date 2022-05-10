import _struct
# Test _struct.Struct.
s = _struct.Struct('i')
s.size
s.format
s.pack(42)
s.unpack(_struct.pack('i', 42))
s.unpack_from(_struct.pack('i', 42), 0)
s.unpack_from(memoryview(_struct.pack('i', 42)), 0)
# Test _struct.pack.
_struct.pack('i', 42)
_struct.pack('ii', 1, 2)
_struct.pack('ii', 1)
_struct.pack('ii', 1, 2, 3)
_struct.pack('ii', (1, 2))
_struct.pack('ii', [1, 2])
_struct.pack('ii', memoryview(b'\x01\x00\x00\x00\x02\x00\x00\x00'))
_struct.pack('ii', b'\x01\x00\x00\x00\x02\x00\x00\x00')
