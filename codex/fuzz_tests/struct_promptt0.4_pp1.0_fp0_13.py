import _struct
# Test _struct.Struct with big endian format.
s = _struct.Struct('>i')
print s.size
print s.pack(1)
print s.unpack(s.pack(1))
print s.unpack(s.pack(1))[0]

# Test _struct.Struct with little endian format.
s = _struct.Struct('<i')
print s.size
print s.pack(1)
print s.unpack(s.pack(1))
print s.unpack(s.pack(1))[0]

# Test _struct.Struct with native format.
s = _struct.Struct('i')
print s.size
print s.pack(1)
print s.unpack(s.pack(1))
print s.unpack(s.pack(1))[0]

# Test _struct.Struct with native format.
s = _struct.Struct('I')
print s.size
print s.pack(1)
print s.unpack(s.pack(1))
print s.unpack(s.pack(1))[0]


