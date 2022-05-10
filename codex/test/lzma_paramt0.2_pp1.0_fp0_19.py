from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 压缩
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'hello world')
compressor.flush()

# 压缩文件
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write('hello world')

# 解压文件
import lzma
with lzma.open('file.xz') as f:
    file_content = f.read()

# 压缩文件
import lzma
with lzma.open('file.xz', 'w') as f:
    f.write(b'hello world')

# 解
