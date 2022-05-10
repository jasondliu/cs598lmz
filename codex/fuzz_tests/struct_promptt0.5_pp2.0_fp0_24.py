import _struct
# Test _struct.Struct
TestStruct = _struct.Struct('i')
print TestStruct.size
print TestStruct.format
print TestStruct.unpack(TestStruct.pack(1))
print TestStruct.unpack_from('\x01\x00\x00\x00', 0)
print TestStruct.unpack_from('\x01\x00\x00\x00', 0, 1)
