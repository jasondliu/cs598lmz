from lzma import LZMADecompressor
LZMADecompressor.decompress(compressed_data)

# 使用压缩文件
import bz2

with bz2.open('file.bz2', 'rt') as f:
    for line in f:
        print(line)

# 使用lzma
import lzma

with lzma.open('file.xz', 'rt') as f:
    for line in f:
        print(line)

# 压缩内存中的数据
import bz2

uncompressed_data = b'Hello World!\n'

compressed = bz2.compress(uncompressed_data)

print(compressed)

print(bz2.decompress(compressed))

# 使用zlib
import zlib

uncompressed_data = b'Hello World!\n'

compressed = zlib.compress(uncompressed_data)

print(compressed)

print(zlib.decompress
