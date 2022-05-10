import _struct
# Test _struct.Struct

# Test the basic methods

s = _struct.Struct("i")

print(s.format)
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# Test the methods on a non-native format

s = _struct.Struct("!i")

print(s.format)
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# Test the methods on a non-native format

s = _struct.Struct("<i")

print(s.format)
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# Test the methods on a non-native format

s = _struct.Struct(">i")

print(s.format)
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

# Test the methods on a non-native format


