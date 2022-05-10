from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

##lzma.open 函数
# 提供读写和流式支持的透明方式
with lzma.open('somefile', 'wt') as f:
    f.write(text)
with lzma.open('somefile', 'rt') as f:
    text = f.read()

import bz2
for line in bz2.open('/etc/passwd', 'rt'):
    print(line)

# bz2.BZ2Compressor 和 bz2.BZ2Decompressor 类
text1 = b'This is the data to compress. '
text2 = b'Working together to compress it more.'

compressor = bz2.BZ2Compressor()
print(compressor.compress(text1))
print(compressor.compress(text2))
print(compressor.flush())

compressed_data = compressor.compress(text2)
