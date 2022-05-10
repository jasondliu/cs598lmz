import _struct
# Test _struct.Struct
#
# XXX: This test is incomplete.  It does not test all functions.

# build a struct from a string

struct1 = _struct.Struct("hhl")

# test pack() and unpack()

packed1 = struct1.pack(1, 2, 3)
print(packed1)
unpacked1 = struct1.unpack(packed1)
print(unpacked1)

# test the size of the struct

print(struct1.size)

# test the format string of the struct

print(struct1.format)

# test the alignment of the struct

print(struct1.alignment)

# test the pack_into() and unpack_from() methods

b = bytearray(struct1.size)
struct1.pack_into(b, 0, 1, 2, 3)
print(b)
print(struct1.unpack_from(b, 0))

# test the pack() and unpack() methods with byteorder

struct1 = _struct.Struct("!hhl")

packed1 = struct1.pack
