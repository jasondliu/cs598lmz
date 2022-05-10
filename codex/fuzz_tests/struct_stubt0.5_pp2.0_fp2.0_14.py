from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# 任意长度的字符串
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack_into(bytearray(12), 0, 1, 'ab'.encode('utf-8'), 2.7)

# 可以在一个字节串中嵌入另一个字节串
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack_into(bytearray(12), 0, 1, b'ab', 2.7)
