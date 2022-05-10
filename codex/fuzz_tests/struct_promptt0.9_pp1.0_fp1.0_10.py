import _struct
# Test _struct.Struct.
f = _struct.Struct("H")
f.size
f.pack_into("", bytearray(x for x in range(7)), 0, 1, 0)
f.unpack_from(bytearray(x for x in range(8)), 6, 0)
f.pack_into("", bytearray(x for x in range(7)), 0, 1, 0)
f.unpack_from(bytearray(x for x in range(8)), 6, 0)
f.pack_into("", bytearray(x for x in range(7)), 0, 1, 0)
f.unpack_from(bytearray(x for x in range(8)), 6, 0)

# Test format push_back. A "Optional_type" is needed to dereference, so
# it is not tested.
f = _struct.Struct("")
for i in range(1, 13):
    f = f + "B"
f.size
f.pack_into("", bytearray(x for x in range(12)), 0, 1
