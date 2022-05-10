import _struct
# Test _struct.Struct

# Create a struct object
s = _struct.Struct('hhl')

# Get the size of the object
print(s.size)

# Pack a tuple into bytes
packed_data = s.pack(1, 2, 3)
print(packed_data)

# Unpack bytes into a tuple
original_data = s.unpack(packed_data)
print(original_data)

# Get the internal format used by the struct object
print(s.format)

# Create a struct object
s = _struct.Struct('hhl')

# Get the size of the object
print(s.size)

# Pack a tuple into bytes
packed_data = s.pack(1, 2, 3)
print(packed_data)

# Unpack bytes into a tuple
original_data = s.unpack(packed_data)
print(original_data)

# Get the internal format used by the struct object
print(s.format)

# Create a struct object
s = _struct.Struct('hhl')

# Get the size of the object
