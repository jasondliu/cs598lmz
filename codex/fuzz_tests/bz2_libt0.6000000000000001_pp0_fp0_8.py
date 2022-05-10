import bz2
bz2.decompress(bz2.compress(data))

# gzip
import gzip
s = b'witch which has which witches wrist watch'
len(s)
t = gzip.compress(s)
len(t)
gzip.decompress(t)

# 通过gzip.compress()进行压缩，并且将压缩后的数据保存到文件中
f = open('compress.txt', 'wb')
f.write(gzip.compress(bytes(range(10))))
f.close()

# 接下来，从文件中读取数据并且解压缩
import gzip
f = gzip.open('compress.txt', 'rb')
f.read()
