import _struct
# Test _struct.Struct.
s = _struct.Struct("l")
s.size
s.format
s.pack(0)
s.pack(1)
s.pack(2)
s.pack(3)
s.unpack(b"\x00\x00\x00\x00\x00\x00\x00\x00")
s.unpack(b"\x00\x00\x00\x00\x00\x00\x00\x01")
s.unpack(b"\x00\x00\x00\x00\x00\x00\x00\x02")
s.unpack(b"\x00\x00\x00\x00\x00\x00\x00\x03")
# Test _struct.Struct.iter_unpack.
s = _struct.Struct("l")
list(s.iter_unpack(b"\x00\x00\x00\x00\x00\x00\x00\x00"))
