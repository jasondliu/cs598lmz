import _struct
# Test _struct.Struct.format_size
print(_struct.Struct("").format_size(""))
print(_struct.Struct("=i").format_size(""))
print(_struct.Struct("=i").format_size("x"))
print(_struct.Struct("=i").format_size("ii"))
print(_struct.Struct("=i").format_size("i" * 10000))
try:
    print(_struct.Struct("=i").format_size("i" * 1000000))
except MemoryError:
    print("MemoryError")

# Test _struct.Struct.size
print(_struct.Struct("").size)
print(_struct.Struct("=i").size)

# Test _struct.pack
print(_struct.pack("=i", 42))
print(_struct.pack("=i", 4294967296))
print(_struct.pack("=i", -1))
print(_struct.pack("=i", -2147483648))
print(_struct.pack("=i", 2147483647))
