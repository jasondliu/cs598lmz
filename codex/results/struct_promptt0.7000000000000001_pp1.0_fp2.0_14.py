import _struct
# Test _struct.Struct.format
print _struct.Struct('cx').format
print _struct.Struct('l').format
print _struct.Struct('d').format
print _struct.Struct('P').format
# Test _struct.Struct.size
print _struct.Struct('cx').size
print _struct.Struct('l').size
print _struct.Struct('d').size
print _struct.Struct('P').size
# Test _struct.Struct.pack
print _struct.Struct('cx').pack('\0')
print _struct.Struct('l').pack(0)
print _struct.Struct('d').pack(0.0)
print _struct.Struct('P').pack(0)
# Test _struct.Struct.unpack
print _struct.Struct('cx').unpack('\0')
print _struct.Struct('l').unpack('\0\0\0\0')
print _struct.Struct('d').unpack('\0\0\0\0\0\0\0\0')
print _struct.Struct('P').unpack('\0\0\0\0\0
