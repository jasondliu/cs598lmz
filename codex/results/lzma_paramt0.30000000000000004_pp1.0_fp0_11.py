from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 压缩数据
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write(text)

# 解压缩数据
import lzma
with lzma.open('file.xz') as f:
    text = f.read()

# 压缩数据
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

# 解压缩数据
import bz2
with bz2.open('file.bz2') as f:
    text = f.read()

# 压缩数据
import gzip
with gzip.open('file.gz', 'wt') as f:
    f.write(text)

# 解压缩数据
import gzip
with gzip.
