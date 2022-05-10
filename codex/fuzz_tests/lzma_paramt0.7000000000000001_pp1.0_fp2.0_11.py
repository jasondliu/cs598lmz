from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# 压缩数据
decompressor = LZMADecompressor()
data = []
for chunk in iter(lambda: file_obj.read(100 * 1024), b''):
    data.append(decompressor.decompress(chunk))

# 压缩数据
decompressor = LZMADecompressor()
for chunk in iter(lambda: file_obj.read(100 * 1024), b''):
    decompressor.decompress(chunk)

# 压缩数据
decompressor = LZMADecompressor()
decompressor.decompress(b'book')
'''

# bz2
'''
import bz2

# 压缩数据
bz2.compress(b'hello world!hello world!hello world!hello world!')

# 解压缩数据
bz2.decompress(b'BZh
