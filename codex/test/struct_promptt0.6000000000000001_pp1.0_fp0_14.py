import _struct
# Test _struct.Struct
struct_test1 = _struct.Struct('hhl')
struct_test1

# Test _struct.pack, _struct.unpack
struct_test2 = _struct.Struct('hhl')
struct_test2.pack(1,2,3)
struct_test2.unpack(b'\x01\x00\x02\x00\x03\x00\x00\x00')

# Test _struct.calcsize
struct_test3 = _struct.Struct('hhl')
struct_test3.calcsize(b'\x01\x00\x02\x00\x03\x00\x00\x00')

# Test _struct.error
struct_test4 = _struct.Struct('hhl')
try:
    struct_test4.unpack(b'\x01\x00\x02\x00\x03\x00\x00\x00\x00\x00')
except:
    pass
