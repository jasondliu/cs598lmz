from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# 分别对应：无符号整数、字符串、浮点数
s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@', 0)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x00@', 4)

# 可以使用buffer对象来替代字节字符串
import array
numbers = array.array('f', (random() for i in range(10**7)))
numbers[-1]

fp = open('data.bin', 'wb')
numbers.tofile(fp)
fp.close()

fp = open('
