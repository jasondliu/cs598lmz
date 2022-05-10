import _struct
# Test _struct.Struct formats
struct_formats = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']

for struct_format in struct_formats:
    s = _struct.Struct(struct_format)
    print('{}: {}'.format(struct_format, s.size))

# A single floating-point value requires 4 bytes
s = _struct.Struct('f')
s.size

# Three floating-point values require 12 bytes
s = _struct.Struct('3f')
s.size

# Values are encoded and decoded as byte arrays
packed = s.pack(1.0, 2.0, 3.0)
packed

s.unpack(packed)

# The '>' indicates that this is a big-endian format
s = _struct.Struct('>i')
s.pack(1)

# '<' indicates little-endian
s = _struct.Struct('<i')
s.pack(1)

# '!' indicates network (big-endian
