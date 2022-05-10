import _struct
# Test _struct.Struct

# Create a struct with format 'hhl'
s = _struct.Struct('hhl')

# Pack values into bytes
packed_data = s.pack(1, 2, 3)

# Unpack values from bytes
unpacked_data = s.unpack(packed_data)

print(packed_data)
print(unpacked_data)

# Create a struct with format 'hhl' and byte order '>'
s = _struct.Struct('>hhl')

# Pack values into bytes
packed_data = s.pack(1, 2, 3)

# Unpack values from bytes
unpacked_data = s.unpack(packed_data)

print(packed_data)
print(unpacked_data)

# Create a struct with format 'hhl' and byte order '<'
s = _struct.Struct('<hhl')

# Pack values into bytes
packed_data = s.pack(1, 2, 3)

# Unpack values from bytes
unpacked_data = s.unpack(packed_data)

