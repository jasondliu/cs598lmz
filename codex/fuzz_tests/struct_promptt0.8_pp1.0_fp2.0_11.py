import _struct
# Test _struct.Struct().iter_unpack() for the empty format
struct = _struct.Struct(b'')
buf = b''
for value in struct.iter_unpack(buf):
    print(value)

# Test size calculation for the empty format
buf = b''
print(struct.calcsize(buf))

# Test _struct.Struct().iter_unpack() for a simple format
struct = _struct.Struct(b'hhl')
buf = b'\x00\x01\x00\x02\x00\x00\x00\x03'
for value in struct.iter_unpack(buf):
    print(value)

# Test size calculation for a simple format
buf = b'\x00\x01\x00\x02\x00\x00\x00\x03'
print(struct.calcsize(buf))

# Test _struct.Struct().iter_unpack() for a simple format with skip
struct = _struct.Struct(b'hh')
buf = b'\x00\x01\x00\x02\x00\x
