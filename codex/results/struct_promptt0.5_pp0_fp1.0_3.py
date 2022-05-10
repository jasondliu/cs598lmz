import _struct
# Test _struct.Struct
test_struct = _struct.Struct('i')
test_struct.size
test_struct.pack(1)
test_struct.unpack(test_struct.pack(1))
test_struct.unpack_from(test_struct.pack(1))
test_struct.iter_unpack(test_struct.pack(1))
# Test _struct.Struct.format
test_struct = _struct.Struct('i')
test_struct.format
test_struct = _struct.Struct('ii')
test_struct.format
test_struct = _struct.Struct('iii')
test_struct.format
test_struct = _struct.Struct('iiii')
test_struct.format
test_struct = _struct.Struct('iiiii')
test_struct.format
test_struct = _struct.Struct('iiiiii')
test_struct.format
test_struct = _struct.Struct('iiiiiii')
test_struct.format
test_struct = _struct.Struct('iiiiiiii')
test_struct.format
test_struct = _struct.Struct('iiiiiiiii')
