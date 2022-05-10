import _struct
# Test _struct.Struct and also module

# Create a test set
format1 = 'hhl5s'
buf1 = b'\x01\x00\x02\x00\x03\x00\x04\x00\x05abcd\x06'

format2 = 'hhl'
buf2 = b'\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00'

format3 = 'hhh'
buf3 = b'\x01\x00\x02\x00\x03\x00'

format4 = 'bchl'
buf4 = b'\x01\x01\x02\x00\x03\x00\x04\x00\x05\x00'

# Test _struct.Struct object
s = _struct.Struct(format1)
print(s.format)
print(s.size)
print(s.pack(*range(1, 6)))
