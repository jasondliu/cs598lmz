import _struct
# Test _struct.Struct("&gt;h") instance with bytes b'\x01\x00\x02\x00'
x = _struct.Struct("&gt;h")

expected = x.unpack_from(b'\x01\x00\x02\x00', 0)
got = x.unpack_from(b'\x01\x00\x02\x00', 0)
print(expected, got)
