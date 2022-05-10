import _struct
# Test _struct.Struct with non-native byte order
s = _struct.Struct('!h')
s.size
s.pack(1)
s.unpack(s.pack(1))
s.unpack(s.pack(1))[0]
s = _struct.Struct('h')
s.size
s.pack(1)
s.unpack(s.pack(1))
s.unpack(s.pack(1))[0]
# Test _struct.Struct with non-native byte order, non-native size
s = _struct.Struct('!l')
s.size
s.pack(1)
s.unpack(s.pack(1))
s.unpack(s.pack(1))[0]
s = _struct.Struct('l')
s.size
s.pack(1)
s.unpack(s.pack(1))
s.unpack(s.pack(1))[0]
# Test _struct.Struct with native byte order, native size
s = _struct.Struct('i')
s.size
s.pack(1)
s.
