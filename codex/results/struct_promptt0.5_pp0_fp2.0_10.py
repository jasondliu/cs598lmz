import _struct
# Test _struct.Struct.__repr__
print(_struct.Struct('h').__repr__())
print(_struct.Struct('h', True).__repr__())
print(_struct.Struct('h', False).__repr__())
print(_struct.Struct('h', True, 'network').__repr__())
print(_struct.Struct('h', False, 'network').__repr__())

# Test _struct.Struct.pack
print(_struct.Struct('h').pack(1))
print(_struct.Struct('h').pack(1, 2))
print(_struct.Struct('h').pack(1, 2, 3))
print(_struct.Struct('h').pack(1, 2, 3, 4))

# Test _struct.Struct.unpack
print(_struct.Struct('h').unpack(b'\x00\x01'))
print(_struct.Struct('h').unpack(b'\x00\x01', 1))
print(_struct.Struct('h').unpack(b'\x00\x01', 1, 2))
print(_struct.Struct('h').unpack(
