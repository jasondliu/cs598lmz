import _struct
# Test _struct.Struct with a fill character
Struct2 = _struct.Struct('B B c 6x B')
s = Struct2.pack(1, 2, 'a', 3)
t = Struct2.unpack(s)
print(t)
# (1, 2, 'a', 3)

# Test _struct.Struct with an odd number of bytes
Struct1 = _struct.Struct('B B c B')
s = Struct1.pack(1, 2, 'a', 3)
t = Struct1.unpack(s)
print(t)
# (1, 2, 'a', 3)
