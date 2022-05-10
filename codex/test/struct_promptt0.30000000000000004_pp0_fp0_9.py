import _struct
# Test _struct.Struct.__repr__
print(_struct.Struct('i').__repr__())
print(_struct.Struct('i').__repr__(1))
# Test _struct.Struct.__str__
print(_struct.Struct('i').__str__())
print(_struct.Struct('i').__str__(1))
# Test _struct.Struct.format
print(_struct.Struct('i').format)
print(_struct.Struct('i').format(1))
# Test _struct.Struct.size
print(_struct.Struct('i').size)
print(_struct.Struct('i').size(1))
# Test _struct.Struct.pack
print(_struct.Struct('i').pack)
print(_struct.Struct('i').pack(1))
# Test _struct.Struct.unpack
print(_struct.Struct('i').unpack)
print(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'))
