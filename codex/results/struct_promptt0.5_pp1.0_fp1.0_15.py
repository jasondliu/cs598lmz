import _struct
# Test _struct.Struct

fmt = "hhl"
s = _struct.Struct(fmt)
print s.size
print s.pack(1, 2, 3)
print s.unpack(s.pack(1, 2, 3))

fmt = "hhl"
s = _struct.Struct(fmt)
print s.size
print s.pack(1, 2, 3)
print s.unpack(s.pack(1, 2, 3))

fmt = "hhl"
s = _struct.Struct(fmt)
print s.size
print s.pack(1, 2, 3)
print s.unpack(s.pack(1, 2, 3))

fmt = "hhl"
s = _struct.Struct(fmt)
print s.size
print s.pack(1, 2, 3)
print s.unpack(s.pack(1, 2, 3))

fmt = "hhl"
s = _struct.Struct(fmt)
print s.size
print s.pack(1, 2, 3)
print s
