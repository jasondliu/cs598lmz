import _struct
# Test _struct.Struct

# Test _struct.Struct.__new__
# Test _struct.Struct.__new__ with invalid format
try:
    _struct.Struct('Z')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct.__new__ with valid format
s = _struct.Struct('i')

# Test _struct.Struct.format
print(s.format)

# Test _struct.Struct.size
print(s.size)

# Test _struct.Struct.pack
print(s.pack(1))

# Test _struct.Struct.pack_into
b = bytearray(s.size)
s.pack_into(b, 0, 1)
print(b)

# Test _struct.Struct.unpack
print(s.unpack(s.pack(1)))

# Test _struct.Struct.unpack_from
print(s.unpack_from(b, 0))

# Test _struct.Struct.iter_unpack
