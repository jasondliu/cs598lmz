from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s)
print(s.size)
print(s.pack(1, b'ab', 2.7))
print(s.unpack(b'\x01ab\x00\x00\x00\x00\x00\x00\xcd\xcc\x8c\x3f'))
print(s.unpack_from(b'\x01ab\x00\x00\x00\x00\x00\x00\xcd\xcc\x8c\x3f', 0))
print(s.unpack_from(b'\x01ab\x00\x00\x00\x00\x00\x00\xcd\xcc\x8c\x3f', 4))

print('-' * 40)

# 格式字符串中的字段名
s = Struct('i2sf')
print(s.unpack(b'\x01
