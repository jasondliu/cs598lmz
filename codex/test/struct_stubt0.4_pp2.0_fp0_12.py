from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

print(s.unpack(b'\x00\x00\x00\x00'))
print(s.unpack(b'\x00\x00\x00\x01'))
print(s.unpack(b'\x00\x00\x00\x02'))
print(s.unpack(b'\x00\x00\x00\x03'))
print(s.unpack(b'\x00\x00\x00\x04'))
print(s.unpack(b'\x00\x00\x00\x05'))
print(s.unpack(b'\x00\x00\x00\x06'))
print(s.unpack(b'\x00\x00\x00\x07'))
print(s.unpack(b'\x00\x00\x00\x08'))
print(s.unpack(b'\x00\x00\x00\t'))

