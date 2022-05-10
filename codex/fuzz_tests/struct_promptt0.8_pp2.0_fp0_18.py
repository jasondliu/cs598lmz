import _struct
# Test _struct.Struct([format])
struct1 = _struct.Struct('=H')
print(struct1)  # test __str__
print(struct1.format)
print(struct1.size)
print(struct1.pack(1))
print(struct1.pack_into(bytearray(4), 0, 1))
try:
    struct.pack_into(bytearray(5), 0, 1)
except struct.error:
    print('struct.error: buffer too small')
print(struct1.unpack(struct1.pack(1)))
print(struct1.unpack_from(struct1.pack(1), 0))
try:
    struct1.unpack_from(struct1.pack(1), 1)
except struct.error:
    print('struct.error: unpack_from requires a buffer of at least 2 bytes')
try:
    struct1.unpack(struct1.pack(1)[0:1])
except struct.error:
    print('struct.error: unpack requires a buffer of at least 2 bytes')
struct1 = _struct.Struct('=
