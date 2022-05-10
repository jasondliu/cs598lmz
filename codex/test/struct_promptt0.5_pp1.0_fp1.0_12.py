import _struct
# Test _struct.Struct.format
print("Test _struct.Struct.format")

s = _struct.Struct("hhl")
print("format:", s.format)
print("size:", s.size)
print("pack_into:", s.pack_into)
print("pack:", s.pack)
print("unpack_from:", s.unpack_from)
print("unpack:", s.unpack)

# Test _struct.Struct.format_code_names
print("\nTest _struct.Struct.format_code_names")

print(s.format_code_names)

# Test _struct.Struct.iter_unpack
print("\nTest _struct.Struct.iter_unpack")

b = s.pack(1, 2, 3)
print(b)

# Test _struct.Struct.iter_unpack
print("\nTest _struct.Struct.iter_unpack")

print(list(s.iter_unpack(b)))

# Test _struct.Struct.iter_unpack_from
