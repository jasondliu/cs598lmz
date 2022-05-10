from lzma import LZMADecompressor
LZMADecompressor().decompress(s)

# 压缩
compressor = LZMACompressor()
compressor.compress(b'Hello World')
compressor.flush()

# 压缩解压缩
compressor = LZMACompressor()
data = b'Hello World'
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = LZMADecompressor()
decompressor.decompress(compressed)

# 压缩率
import sys
sys.getsizeof(b'Hello World')
sys.getsizeof(compressed)

# 压缩多个文件
import lzma
with lzma.open('data.xz', 'wt') as f:
    f.write('Hello World')

with lzma.open('data.xz', 'rt') as f:
    print(f.read())

# 压缩率
import sys
sys.getsizeof('
