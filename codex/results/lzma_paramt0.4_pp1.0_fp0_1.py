from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用LZMA算法压缩数据
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b"some data")
compressor.flush()

# 压缩文件
import lzma
with lzma.open("somefile.xz", "wt") as f:
    f.write("hello world")

# 解压文件
import lzma
with lzma.open("somefile.xz", "rt") as f:
    file_content = f.read()

# bz2模块
import bz2
bz2.compress(b"some data")
bz2.decompress(b"some data")

# 压缩文件
import bz2
with bz2.open("somefile.bz2", "wt") as f:
    f.write("hello world")

