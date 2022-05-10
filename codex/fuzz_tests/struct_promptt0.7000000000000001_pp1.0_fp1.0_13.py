import _struct
# Test _struct.Struct
fmt = 'hhl'
s = _struct.Struct(fmt)
print(s.size)
print(s.pack(1, 2, 3))
print(s.unpack(s.pack(1, 2, 3)))
# Test _struct.pack
print(_struct.pack('>hhl', 1, 2, 3))
print(_struct.pack('>hhl', 1, 2, 3) == s.pack(1, 2, 3))
# Test _struct.unpack
print(_struct.unpack('>hhl', _struct.pack('>hhl', 1, 2, 3)))
print(_struct.unpack('>hhl', _struct.pack('>hhl', 1, 2, 3)) == s.unpack(s.pack(1, 2, 3)))
print(_struct.unpack('>hhl', s.pack(1, 2, 3)))
print(_struct.unpack('>hhl', s.pack(1, 2, 3)) == s.unpack(s.pack(1, 2, 3)))
# Test _struct.calcsize
