import _struct
# Test _struct.Struct

# Create a struct object
s = _struct.Struct('i')

# Size of the struct
print(s.size)

# Pack an integer into the struct
packed = s.pack(123)

# Unpack the struct
print(s.unpack(packed))

# Use the struct to parse a binary file
with open('test.bin', 'rb') as f:
    data = f.read(s.size)
    print(s.unpack(data))

# Create a struct for a C long long
s = _struct.Struct('q')

# Pack a Python int into the struct
packed = s.pack(123)

# Unpack the struct into a Python int
print(s.unpack(packed))

# Create a struct for a C double
s = _struct.Struct('d')

# Pack a Python float into the struct
packed = s.pack(123.456)

# Unpack the struct into a Python float
print(s.unpack(packed))

# Create a struct for a C string
s = _struct.Struct('s
