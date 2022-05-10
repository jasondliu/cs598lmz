from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'hello world!hello world!hello world!hello world!hello world!hello world!hello world!hello world!'

# 如果数据压缩后的长度没有变化，那么压缩算法会拒绝压缩数据并抛出 LZMAError 异常：

data = b'hello world!hello world!hello world!hello world!'

from lzma import LZMACompressor
LZMACompressor().compress(data)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/lzma.py", line 532, in compress
#     return self.compress(data)[0]
#   File "/usr/lib/python3.6/lzma.py", line 5
