import _struct
# Test _struct.Struct
struct = _struct.Struct('=hhl')
data = struct.pack(1, 2, 3)
struct.unpack(data)
# Test _struct.Struct.format
struct = _struct.Struct('<HHHHHHHH')
struct.format
struct.format = '>HHHHHHHH'
struct.format
struct.format = '=HHHHHHHH'
struct.format
# Test _struct.Struct.size
assert struct.size == 32
struct = _struct.Struct('<HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
assert struct.size == 64
# Test _struct.Struct.pack
struct = _struct.Struct('<HHHHHHHH')
data = struct.pack(1, 2, 3, 4, 5, 6, 7, 8)
struct.unpack(data)
# Test _struct.Struct.unpack
struct = _struct.Struct('<HHHHHHHH')
data = struct.pack(1, 2, 3, 4, 5, 6, 7, 8)
struct.unpack(data)
# Test _struct.Struct.pack_into
struct = _struct.Struct('<HHHHHHHH')

