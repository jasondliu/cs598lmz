import _struct
# Test _struct.Struct()
s = _struct.Struct("x y z")
packed = s.pack(1, 2, 3.0)
print s.unpack(packed)
print s.unpack_from(packed, 0), packed
print s.unpack_from(packed, 1), packed[1:]
print s.unpack_from(packed, 2), packed[2:]
print s.unpack_from(packed, 3), packed[3:]
print s.unpack_from(packed, 4), packed[4:]
print s.unpack_from(packed, 5), packed[5:]

# Test bytearray(packed)
packedbytearray = bytearray(packed)
print s.unpack(packedbytearray)
print s.unpack_from(packedbytearray, 0), packed
print s.unpack_from(packedbytearray, 1), packed[1:]
print s.unpack_from(packedbytearray, 2), packed[2:]
print s.unpack_from(packedbytearray, 3), packed[3:]

