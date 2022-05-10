import _struct
# Test _struct.Struct.pack() interface.
packed = Struct.pack(format, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)
assert len(packed) == calcsize(format)
# Test _struct.Struct.unpack() interface.
unpacked = Struct.unpack(format, packed)
assert unpacked == (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)
# Test _struct.pack() function.
packed = _struct.pack(format, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)
assert packed == Struct.pack(format, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)
# Test _struct.unpack() function.
unpacked = _struct.unpack(format, packed)
