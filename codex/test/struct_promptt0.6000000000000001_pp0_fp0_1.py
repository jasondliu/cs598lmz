import _struct
# Test _struct.Struct
struct = _struct.Struct('x')
print(struct)

# Test _struct.calcsize
struct = _struct.Struct('i')
print(struct.size)

# Test _struct.pack
struct = _struct.Struct('i')
packed = struct.pack(1)
print(packed)

# Test _struct.unpack
struct = _struct.Struct('i')
unpacked = struct.unpack(b'\x01\x00\x00\x00')
print(unpacked)

# Test _struct.iter_unpack
struct = _struct.Struct('i')
iter_unpacked = struct.iter_unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00')
print(list(iter_unpacked))
