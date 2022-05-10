import _struct
# Test _struct.Struct
with _struct.Struct(b'i'):
    pass

# Test _struct.Struct.pack
with _struct.Struct(b'i') as struct:
    struct.pack(1)

# Test _struct.Struct.unpack
with _struct.Struct(b'i') as struct:
    struct.unpack(b'\x04\x00\x00\x00')

# Test _struct.Struct.iter_unpack
with _struct.Struct(b'i') as struct:
    for _ in struct.iter_unpack(b'\x04\x00\x00\x00'):
        pass

# Test _struct.Struct.size
with _struct.Struct(b'i') as struct:
    struct.size
