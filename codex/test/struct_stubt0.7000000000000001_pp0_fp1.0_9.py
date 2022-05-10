from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('')
s.size
# 30

s.format = 'i 3s f'
s.size
# 16

s.pack(1, b'foo', 3.14)
# b'\x01\x00\x00\x00foo\x00\x00\x00\x00\x00\x00\xdb\x40\x00\x00'

s.unpack(_)
# (1, b'foo', 3.14)

s.format = 'i 3s f 8x'
s.pack(1, b'foo', 3.14)
# b'\x01\x00\x00\x00foo\x00\x00\x00\x00\x00\x00\xdb\x40\x00\x00\x00\x00\x00\x00'

s.unpack(_)
# (1, b'foo', 3.14)

# 可以使用">"来指定大端模
