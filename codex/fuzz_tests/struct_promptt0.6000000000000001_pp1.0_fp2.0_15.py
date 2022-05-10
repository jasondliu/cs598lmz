import _struct
# Test _struct.Struct
print _struct.Struct('i').pack(100)
print _struct.Struct('3i').pack(100, 200, 300)
print _struct.Struct('3i').pack(*(100, 200, 300))
print _struct.Struct('3i').unpack(_struct.Struct('3i').pack(100, 200, 300))
print _struct.Struct('3i').unpack(_struct.Struct('3i').pack(100, 200, 300)) == (100, 200, 300)
print _struct.Struct('3i').size == 12
print _struct.Struct('i').size == _struct.calcsize('i')
print _struct.Struct('3i').size == _struct.calcsize('3i')
# Test _struct.pack
print _struct.pack('i', 100) == _struct.Struct('i').pack(100)
print _struct.pack('i', 100, 200) == _struct.Struct('i').pack(100, 200)
print _struct.pack('3i', 100, 200, 300) == _struct.Struct('3i').pack(100, 200
