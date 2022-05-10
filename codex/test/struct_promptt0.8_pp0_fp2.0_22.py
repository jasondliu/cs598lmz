import _struct
# Test _struct.Struct
try:
    s = _struct.Struct('i')
    print(s)
    print(s.format)
    print(s.size)
    print(s.unpack_from(b'abcdef', 1))
    print(s.pack(42) + b'abc')
except Exception as e:
    print(e)

print('test_struct_import: {0}'.format(test_struct_import))

print('test_struct_import_submodule: {0}'.format(test_struct_import_submodule))

print('test_struct_import_submodule_subsubmodule: {0}'.format(test_struct_import_submodule_subsubmodule))

print('test_struct_import_subsubmodule: {0}'.format(test_struct_import_subsubmodule))

