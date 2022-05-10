import _struct
# Test _struct.Struct() and _struct.unpack()

assert(_struct.Struct('i').size == 4)
assert(_struct.Struct('ii').size == 8)
assert(_struct.Struct('i').pack(1) == b'\x01\x00\x00\x00')
assert(_struct.Struct('i').pack(0x10000) == b'\x00\x00\x01\x00')
assert(_struct.Struct('i').pack(0x1000000) == b'\x00\x00\x00\x01')
assert(_struct.Struct('i').unpack(b'\x01\x00\x00\x00') == (1,))
assert(_struct.Struct('i').unpack(b'\x00\x00\x01\x00') == (0x10000,))
assert(_struct.Struct('i').unpack(b'\x00\x00\x00\x01') == (0x1000000,))

assert(_struct.Struct('i').size == 4)
assert(_struct.Struct('ii').size == 8)

