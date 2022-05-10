from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 二进制和ASCII等的互相转换
s = b'hello'
import array
a = array.array('B',s)
a
# array('B', [104, 101, 108, 108, 111])
import binascii
binascii.hexlify(a)

# 字节字符串上的字符串操作
data = b'some bytes'
data
# b'some bytes'
data[0:4]
# b'some'
data.startswith(b'some')
# True
data.split()
# [b'some', b'bytes']
data.replace(b'byte',b'tiny')
# b'some tines'
data
# b'some bytes'
# 可以在此类字符串上使用正则表达式、
