from lzma import LZMADecompressor
LZMADecompressor().decompress(open("E:\Python\Python37-32\i.zip","rb").read())

#暴力破解算法
import itertools

chars = '0123456789'
for i in range(6):
    for item in itertools.product(chars, repeat=i):
        a = ''.join(item)
        print(a)

#工具类法
import itertools

chars = '0123456789'
for i in range(6):
    for item in itertools.product(chars, repeat=i):
        a = ''.join(item)
        print(a)

# 字典破解
import itertools

chars = '0123456789'
for i in range(6):
    for item in itertools.product(chars, repeat=i):
        a = ''.join(item)
        print(a)

# 字典
