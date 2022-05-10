import _struct
# Test _struct.Struct()
obj = _struct.Struct("i")
obj.size
obj.format
# Test _struct.Struct.pack()
obj.pack(1234)
obj.pack(-123456789)
# Test _struct.Struct.unpack()
obj.unpack(b'\xd2\x04\x00\x00')[0]
obj.unpack(b'\x2d\xfe\xca\x00')[0]
# Test _struct.unpack()
_struct.unpack("i", b'\xd2\x04\x00\x00')[0]
_struct.unpack("i", b'\x2d\xfe\xca\x00')[0]
# Test _struct.pack()
_struct.pack("i", 1234)
_struct.pack("i", -123456789)
# Test _struct.calcsize()
_struct.calcsize("i")
# Test _struct.iter_unpack()
list(_struct.iter_unpack("i", b'\xde\xad\
