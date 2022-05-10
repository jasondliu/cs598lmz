import _struct
# Test _struct.Struct
for fmt, size in (('b', 1), ('B', 1), ('h', 2), ('H', 2), ('i', 4), ('I', 4), ('q', 8), ('Q', 8), ('n', 2), ('N', 4)):
    assert _struct.Struct(fmt).size == size

# Test struct.unpack
assert _struct.unpack('b', b'\x01') == (1,)
assert _struct.unpack('B', b'\x01') == (1,)
assert _struct.unpack('h', b'\x01\x02') == (258,)
assert _struct.unpack('H', b'\x01\x02') == (258,)
assert _struct.unpack('i', b'\x01\x02\x03\x04') == (16909060,)
assert _struct.unpack('I', b'\x01\x02\x03\x04') == (16909060,)
assert _struct.unpack('l', b'\x01\x02\x03\x04') == (169
