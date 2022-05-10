import _struct
# Test _struct.Struct
# 0 means little-endian, 1 means big-endian
s = _struct.Struct('>I')
packed_data = s.pack(12345)
print(packed_data)

# The '<' means endianness is little
print(_struct.unpack('<I', packed_data))

# Length of the struct
print(s.size)

# Default size is 1 byte
s = _struct.Struct('>B')
print(s.size)

# Memoryview allows you to have a slice of a byte string without having to
# create a new one
packed_data = s.pack(255)
mv = memoryview(packed_data)
print(mv)

# Can slice it
print(mv[0])

# Can slice it with a start and end value
print(mv[0:1])

# Can convert it to a different type
print(mv[0:1].tobytes())

# Can make changes to a memoryview and it will change the underlying packed
# data
mv[0] = 1
print(
