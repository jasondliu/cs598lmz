from lzma import LZMADecompressor
LZMADecompressor().decompress(open('data/compressed_data', 'rb').read())

# 使用LZMA压缩文件
import lzma
with lzma.open('data/compressed_data', 'wt') as f:
    f.write(text)

# LZMA的压缩率和速度稍微比gzip略好，但是不是很多。
# 另外一个压缩和解压程序就是bz2模块。
import bz2
with bz2.open('data/compressed_data', 'wt') as f:
    f.write(text)
f = bz2.open('data/compressed_data')
f.read()

# bz2模块提供了一个BZ2Compressor和BZ2Decompressor
