import _struct
# Test _struct.Struct

# Some structs to use
s = _struct.Struct('i')
s2 = _struct.Struct('hh')
s3 = _struct.Struct('hhh')

# Format 'i'
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))
print(s.unpack_from(s.pack(1), 0))

# Format 'hh'
print(s2.size)
print(s2.pack(1, 2))
print(s2.unpack(s2.pack(1, 2)))
print(s2.unpack_from(s2.pack(1, 2), 0))

# Format 'hhh'
print(s3.size)
print(s3.pack(1, 2, 3))
print(s3.unpack(s3.pack(1, 2, 3)))
print(s3.unpack_from(s3.pack(1, 2, 3), 0))

# Format 'hhh' with offset
