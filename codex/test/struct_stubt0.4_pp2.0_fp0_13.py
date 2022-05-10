from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('=2s2s')
print(s.size)
print(s.pack(b'ab', b'cd'))
print(s.unpack(b'abcd'))

# 创建一个结构，包含3个字节的整数和一个字节的字符串
s = Struct.__new__(Struct)
s.__init__('<3i1s')
print(s.size)
print(s.pack(1, 2, 3, b'ab'))
print(s.unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00ab'))

