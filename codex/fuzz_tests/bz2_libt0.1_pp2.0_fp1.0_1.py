import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
with bz2.BZ2File('spam.bz2', 'wb') as f:
    f.write(b'Hello World')

with bz2.BZ2File('spam.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
import gzip
with gzip.open('spam.gz', 'wt') as f:
    f.write('Hello World')

with gzip.open('spam.gz', 'rt') as f:
    print(f.read())

# 压缩文件
import lzma
with lzma.open('spam.xz', 'wt') as f:
    f.write('Hello World')

with lzma.open('spam.xz', 'rt') as f:
    print(f.read())

# 压缩文件
