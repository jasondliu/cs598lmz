import _struct
# Test _struct.Struct
struct = _struct.Struct('hhl')
values = (1, 2, 3)
s = struct.pack(*values)
print(repr(s))
print(struct.unpack(s))

# Test _struct.Struct.unpack_from and pack_into
s = struct.pack(1, 2, 3)
print(struct.unpack_from(s, 0))
print(struct.unpack_from(s, 1))
print(struct.unpack_from(s, 2))
buf = bytearray(b'\0' * struct.size)
struct.pack_into(buf, 0, 1, 2, 3)
print(struct.unpack_from(buf, 0))
struct.pack_into(buf, 1, 1, 2, 3)
print(struct.unpack_from(buf, 1))
struct.pack_into(buf, 2, 1, 2, 3)
print(struct.unpack_from(buf, 2))

# Test _struct.Struct.__getitem__
struct = _struct.Struct('h')
buf
