import _struct
# Test _struct.Struct.

# Test basic packing and unpacking.
s = _struct.Struct('i')
packed = s.pack(10)
unpacked = s.unpack(packed)
assert packed == b'\n\x00\x00\x00'
assert unpacked == (10,)

# Test packing and unpacking with format string that uses '='
s = _struct.Struct('=i')
packed = s.pack(10)
unpacked = s.unpack(packed)
assert packed == b'\n\x00\x00\x00'
assert unpacked == (10,)

# Test packing and unpacking with format string that uses '@'
s = _struct.Struct('@i')
packed = s.pack(10)
unpacked = s.unpack(packed)
assert packed == b'\n\x00\x00\x00'
assert unpacked == (10,)

# Test packing and unpacking with format string that uses '<'
s = _struct.Struct('<i')
packed = s.pack(10)
unpacked = s.unpack
