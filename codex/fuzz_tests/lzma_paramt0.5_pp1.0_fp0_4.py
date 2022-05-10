from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# 使用bz2压缩数据
import bz2
original_data = b'This is the original text.'
print(len(original_data))
# 25
compressed = bz2.compress(original_data)
print(len(compressed))
# 17
decompressed = bz2.decompress(compressed)
print(decompressed)
# b'This is the original text.'

# 创建bz2压缩对象并对数据进行压缩
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'This is the original text.')
# b'BZh91AY&SY.\xc4V\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\
