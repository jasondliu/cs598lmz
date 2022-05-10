import _struct
# Test _struct.Struct.
struct = _struct.Struct(b'h')
struct.pack(13)
struct.pack(-2)
struct.unpack(b'\x00\x0d')
struct.unpack(b'\xff\xfe')
struct.unpack(b'\x00\x0d\xff\xfe')
struct.unpack(b'\x00\x0d\xff')
