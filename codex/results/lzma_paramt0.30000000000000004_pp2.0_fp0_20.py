from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 压缩
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'Some data')
compressor.flush()

# 解压缩
from lzma import LZMADecompressor
decompressor = LZMADecompressor()
decompressor.decompress(b'...')
decompressor.unused_data

# 压缩文件
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write(text)

# 解压缩文件
import lzma
with lzma.open('file.xz') as f:
    text = f.read()

# 压缩文件
import lzma
with lzma.open('file.xz', 'wb') as f:
    f.write(data)

# 解压缩
