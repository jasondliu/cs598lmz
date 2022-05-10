from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 3s f')
print(s.size)
# 10
print(s.pack(1, b'abc', 2.7))
# b'\x01abc\x00\x00\x00\x00\x00\x00\x00@A\xbf?'
print(s.unpack(b'\x01abc\x00\x00\x00\x00\x00\x00\x00@A\xbf?'))
# (1, b'abc', 2.699999988079071)

# 编码与解码
print('abc'.encode('utf-8'))
# b'abc'
print(b'abc'.decode('utf-8'))
# abc

# 压缩与解压缩
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
# 41
t = zlib.compress(s)
print(len(t))
#
