import bz2
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# bz2.compress(b'hello world!')


# 如果一个文件使用bz2压缩过，那么读取的时候，必须先解压
with bz2.BZ2File('example.bz2') as f:
    print(f.read())

# 如果要压缩文件，可以这样写
data = b'hello world!hello world!hello world!hello world!'
with bz2.BZ2File('example.b
