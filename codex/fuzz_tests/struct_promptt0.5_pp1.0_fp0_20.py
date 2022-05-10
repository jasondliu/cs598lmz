import _struct
# Test _struct.Struct.

# Verify that _struct.Struct can be used to create structs with standard
# format characters.

s = _struct.Struct('bBhHiIlLqQfd')

# Test packing.
values = (1, 2, -3, -4, 5, 6, 7, -8, -9, 10.0, 11.0)
for v in values:
    assert s.pack(v) == struct.pack('bBhHiIlLqQfd', v)

# Test unpacking.
s = _struct.Struct('bBhHiIlLqQfd')
packed = s.pack(*values)
assert s.unpack(packed) == values

# Test packing and unpacking with endianness.
s = _struct.Struct('<bBhHiIlLqQfd')
packed = s.pack(*values)
assert s.unpack(packed) == values

s = _struct.Struct('>bBhHiIlLqQfd')
packed = s.pack(*values)
assert s.unpack(packed) == values

# Verify
