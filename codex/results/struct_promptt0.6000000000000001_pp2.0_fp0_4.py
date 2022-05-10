import _struct
# Test _struct.Struct()
struct = _struct.Struct('i')
struct.size
struct.pack(42)
struct.pack(42).unpack(struct.format)
struct.pack(42).unpack(struct.format)[0]
struct.pack(42).unpack(struct.format)[0] == 42
struct.pack('>i', 42)
struct.pack('>i', 42).unpack('>i')
struct.pack('>i', 42).unpack('>i')[0]
struct.pack('>i', 42).unpack('>i')[0] == 42

# Test _struct.pack()
_struct.pack('i', 42)
_struct.pack('>i', 42)
_struct.pack('>i', 42).unpack('>i')
_struct.pack('>i', 42).unpack('>i')[0]
_struct.pack('>i', 42).unpack('>i')[0] == 42

# Test _struct.unpack()
_struct.unpack('>i', _struct.pack('>i', 42))

