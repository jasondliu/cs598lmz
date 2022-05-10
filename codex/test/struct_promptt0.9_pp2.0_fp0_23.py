import _struct
# Test _struct.Struct
# Create object f
f = _struct.Struct('f')
print(f.format)
print(f.size)
# Before pack
print(f.pack(1.33))
# Create object i
i = _struct.Struct('i')
print(i.format)
print(i.size)
# Before pack
print(i.pack(42))
print(type(i.pack(42)))
