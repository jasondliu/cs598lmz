from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('test.bz2','rb').read()).decode()

# 使用 gzip 模块
import gzip
f = gzip.open('test.gz','rb')
f.read()

# 使用 zipfile 模块
import zipfile
z = zipfile.ZipFile('test.zip','r')
z.extractall(path='.')

# 压缩文件
import gzip
with gzip.open('test.gz','wb') as f:
    f.write(b'hello,world!')

# zlib 模块
import zlib
s = b'hello,world!'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)

# 压缩级别
zlib.compress(s,9)

# 校验和
zlib.crc32(s)

# 结
