from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 6.6.1.6.2. ZLIB 圧縮
import zlib
data = b'witch which has which witches wrist watch'
len(data)
compressed = zlib.compress(data)
len(compressed)
compressed
zlib.decompress(compressed)

# 6.6.1.6.3. LZMA 圧縮
import lzma
data = b'witch which has which witches wrist watch'
len(data)
compressed = lzma.compress(data)
len(compressed)
compressed
lzma.decompress(compressed)

# 6.6.1.7. 圧縮ファイルの読み書き
# 6.6.1.7.1. gzip 圧縮ファイル
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz',
