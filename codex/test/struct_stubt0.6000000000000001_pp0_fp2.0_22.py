from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)
print(s.pack(1, b'ab', 2.7))
print(s.unpack(b'\x01ab\x00\x00\x00\x00\x00\x00\xcd@'))
print(s.unpack_from(b'\x01ab\x00\x00\x00\x00\x00\x00\xcd@', 4))

# struct.iter_unpack(fmt, buffer)
# struct.iter_unpack_from(fmt, buffer, offset=0)
s = Struct('I 2s f')
for rec in zip(*[iter(s.unpack_from, b'')] * s.size):
    print(rec)

# 使用bytes对象
print(b'ACME', 50, 91.5)
print(b'ACME', 50, 91.5, sep=',')
