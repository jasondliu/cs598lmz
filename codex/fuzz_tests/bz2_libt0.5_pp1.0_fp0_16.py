import bz2
bz2.decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# 使用bz2.compress()函数压缩数据
data = bz2.compress(b'hello world')
print(data)
bz2.decompress(data)

# bz2.compress()函数的压缩率比zlib.compress()函数的压缩率要高得多，但是压缩和解压缩的速度也比zlib.compress()函数的速度要慢得多，因此，如果压缩的
