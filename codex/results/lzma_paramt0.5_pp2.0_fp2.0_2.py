from lzma import LZMADecompressor
LZMADecompressor().decompress(b'...')

# 使用LZMACompressor来压缩数据
from lzma import LZMACompressor
compressor = LZMACompressor()
data = b'...'
compressor.compress(data)
compressor.flush()

# 压缩和解压文件
import lzma
with lzma.open('lzma_compressed.xz', 'wt') as f:
    f.write(text)

with lzma.open('lzma_compressed.xz', 'rt') as f:
    text = f.read()

# 使用bz2压缩数据
import bz2
bz2.compress(b'...')
bz2.decompress(b'...')

# 使用BZ2Compressor和BZ2Decompressor来压缩和解压数
