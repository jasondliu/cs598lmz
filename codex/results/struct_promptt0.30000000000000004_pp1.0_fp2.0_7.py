import _struct
# Test _struct.Struct

# Test packing
s = _struct.Struct('i')
assert s.pack(1) == b'\x01\x00\x00\x00'
assert s.pack(1, 2) == b'\x01\x00\x00\x00'
assert s.pack(1, 2, 3) == b'\x01\x00\x00\x00'
assert s.pack(1, 2, 3, 4) == b'\x01\x00\x00\x00'
assert s.pack(1, 2, 3, 4, 5) == b'\x01\x00\x00\x00'
assert s.pack(1, 2, 3, 4, 5, 6) == b'\x01\x00\x00\x00'
assert s.pack(1, 2, 3, 4, 5, 6, 7) == b'\x01\x00\x00\x00'

# Test unpacking
assert s.unpack(b'\x01\x00\x00\x00') == (1
