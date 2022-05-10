import _struct
# Test _struct.Struct
struct = _struct.Struct('i')
struct.size
struct.pack(42)
struct.unpack(struct.pack(42))
struct.unpack(struct.pack(42))[0]
struct.unpack(struct.pack(42))[0] == 42
struct.unpack(struct.pack(42))[0] == 43
struct.unpack('\x00\x00\x00*')[0]
struct.unpack('\x00\x00\x00*')[0] == 42
struct.unpack('\x00\x00\x00*')[0] == 43
struct.unpack('\x00\x00\x00*')
struct.unpack('\x00\x00\x00*')[0]
struct.unpack('\x00\x00\x00*')[0] == 42
struct.unpack('\x00\x00\x00*')[0] == 43
struct.unpack('\x00\x00\x00*')
struct.unpack('\x00\x00
