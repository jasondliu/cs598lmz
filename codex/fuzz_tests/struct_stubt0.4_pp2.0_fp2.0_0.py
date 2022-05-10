from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

s.unpack(_)

s.unpack_from(bytes, 0)

s.unpack_from(bytes, 4)

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
octets

import struct
struct.unpack('>5h', octets)

# 字符串和字节序列
# 在Python 3中，字符串和字节序列是不同的类型。
# 字节序列是bytes，而不是str。
# 字符串是Unicode序列，而不是字节序列。

#
