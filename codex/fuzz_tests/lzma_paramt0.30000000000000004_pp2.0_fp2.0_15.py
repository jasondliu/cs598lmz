from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用lzma.LZMAFile()读取压缩文件
import lzma
with lzma.open('example.xz', 'rt') as f:
    text = f.read()

# 使用bz2模块压缩数据
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'Hello World!')
compressor.flush()

# 使用bz2.BZ2File()读取压缩文件
import bz2
with bz2.open('example.bz2', 'rt') as f:
    text = f.read()

# 使用zlib模块压缩数据
import zlib
compressor = zlib.compressobj(1)
compressor.compress(b'Hello World!')
compressor.flush()

