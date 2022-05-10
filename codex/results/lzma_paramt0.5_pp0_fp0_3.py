from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 把解压缩的数据写入文件
with open('decompress.txt', 'wb') as f:
    f.write(decompressed)

# 完整的压缩解压缩过程
import bz2
compressor = bz2.BZ2Compressor()
with open('compress.txt', 'wb') as f:
    for data in iter(lambda : f.read(100), b''):
        compressed = compressor.compress(data)
        if compressed:
            f.write(compressed)
        else:
            break
    f.write(compressor.flush())

# 压缩文件的阅读器
import bz2
uncompressor = bz2.BZ2Decompressor()
with open('compress.txt', 'rb') as f:
    with open('uncompress.txt', 'wb') as g:
