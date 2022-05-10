from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)
# 12

print(s.pack(1, b'ab', 2.7))
# b'\x01ab\x00\x00\x00\x00\x00\x00(B'

print(s.unpack(b'\x01ab\x00\x00\x00\x00\x00\x00(B'))
# (1, b'ab', 2.700000047683716)

print(s.unpack_from(b'\x01ab\x00\x00\x00\x00\x00\x00(B', 4))
# (b'ab', 2.700000047683716)

s = Struct('I 2s f')
print(s.unpack_from(b'\x01ab\x00\x00\x00\x00\x00\x00(B', 4))
# (b'ab', 2.700000047683716
