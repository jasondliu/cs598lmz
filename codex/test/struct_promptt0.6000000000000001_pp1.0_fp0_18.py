import _struct
# Test _struct.Struct
struct = _struct.Struct("hhl")
data = struct.pack(1, 2, 3)
print(data)
print(struct.unpack(data))
struct.unpack_from(data)
