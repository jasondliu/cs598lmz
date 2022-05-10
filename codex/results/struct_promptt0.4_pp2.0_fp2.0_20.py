import _struct
# Test _struct.Struct.format_size
print _struct.Struct('i').format_size('@')
print _struct.Struct('i').format_size('<')
print _struct.Struct('i').format_size('>')
print _struct.Struct('i').format_size('=')
# Test _struct.Struct.size
print _struct.Struct('i').size
# Test _struct.Struct.pack
print _struct.Struct('i').pack(1)
# Test _struct.Struct.unpack
print _struct.Struct('i').unpack(_struct.Struct('i').pack(1))
# Test _struct.Struct.iter_unpack
print list(_struct.Struct('i').iter_unpack(_struct.Struct('i').pack(1)))
# Test _struct.Struct.unpack_from
print _struct.Struct('i').unpack_from(_struct.Struct('i').pack(1), 0)
# Test _struct.Struct.iter_unpack_from
print list(_struct.Struct('i').iter_unpack_from(_struct.Struct('i').pack(1), 0))

