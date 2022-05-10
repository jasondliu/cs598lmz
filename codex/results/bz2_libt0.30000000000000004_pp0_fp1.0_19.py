import bz2
bz2.decompress(bz2.compress(b'Hello World'))

# 压缩文件
with bz2.open('test.txt.bz2', 'wb') as f:
    f.write(b'Hello World')

with bz2.open('test.txt.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
import gzip
with gzip.open('test.txt.gz', 'wb') as f:
    f.write(b'Hello World')

with gzip.open('test.txt.gz', 'rb') as f:
    print(f.read())

# 压缩文件
import lzma
with lzma.open('test.txt.xz', 'wb') as f:
    f.write(b'Hello World')

with lzma.open('test.txt.xz', 'rb') as f:
    print(f.read())
