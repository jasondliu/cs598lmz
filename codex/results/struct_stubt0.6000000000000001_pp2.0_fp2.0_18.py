from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = calcsize(s.format)

x = 0x61626364
# x = 0x61626364
print(s.pack(x))

# b'abcd'
# b'\x00\x00\x00\x00'
# b'\x00\x00\x00d'

# b'\x00\x00\x00d'
# b'\x00\x00\x00\x00'
# b'abcd'

# b'\x00\x00\x00\x00'
# b'abcd'
# b'\x00\x00\x00d'
