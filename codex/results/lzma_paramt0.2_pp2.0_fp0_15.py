from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用LZMA算法压缩数据
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'Binary data')
compressor.flush()

# 压缩文件
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write(text)

# 解压文件
import lzma
with lzma.open('file.xz') as f:
    text = f.read()

# 压缩和解压缩数据
import bz2
bz2.compress(b'Binary data')
bz2.decompress(b'Binary data')

# 压缩文件
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.
