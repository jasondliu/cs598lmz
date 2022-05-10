import _struct
# Test _struct.Struct()
format = "bhilfd"
s = _struct.Struct(format)
s2 = _struct.Struct(s.format)
assert s.format == s2.format == format

# Test standard packing, native and standard size
assert s.size == (1 + 2 + 4 + 4 + 8)
assert s.pack(*range(6)) == _struct.pack(format, *range(6))
assert s.pack(1,2,3,4,5,6) == _struct.pack(format, 1,2,3,4,5,6)
# Test standard packing, non-native
format = "!bhilfd"
s = _struct.Struct(format)
assert s.size == (1 + 2 + 4 + 4 + 8)
assert s.pack(*range(6)) == _struct.pack(format, *range(6))
assert s.pack(1,2,3,4,5,6) == _struct.pack(format, 1,2,3,4,5,6)

# Test standard packing, standard size and alignment
format = "<bhil
