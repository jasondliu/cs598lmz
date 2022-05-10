import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 字符串压缩
import zlib
zlib.compress(b'hello world')
zlib.decompress(zlib.compress(b'hello world'))

# 压缩文件
import gzip
with gzip.open('/tmp/test.gz', 'wt') as f:
    f.write('hello world')
with gzip.open('/tmp/test.gz', 'rt') as f:
    print(f.read())

# 压缩文件
import bz2
with bz2.open('/tmp/test.bz2', 'wt') as f:
    f.write('hello world')
with bz2.open('/tmp/test.bz2', 'rt') as f:
    print(f.read())

# 压缩文件
import lzma
with lzma.open('/tmp/test.xz
